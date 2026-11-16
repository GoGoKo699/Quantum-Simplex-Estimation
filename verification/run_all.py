#!/usr/bin/env python3
"""Finite checks of the simplex estimator and its controlled LCU/RUS primitive.

This is a deterministic floating-point check, not a proof certificate or a
simulation of a noisy device. No probability cutoffs discard rare outcomes.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from functools import lru_cache
import hashlib
import json
from pathlib import Path
import platform

import numpy as np


@lru_cache(maxsize=None)
def sine_law(q: float, m: int) -> tuple[np.ndarray, np.ndarray]:
    """Compute the law from the clock's Fourier/DST amplitudes.

    The exact endpoint laws are used to avoid floating-point leakage into an
    impossible zero-mass subtree. Interior probabilities are never thresholded.
    m=0 means one ordinary conditional specimen, measured as Bernoulli(q).
    """
    if m == 0:
        return np.array([0.0, 1.0]), np.array([1.0-q, q])
    assert m >= 3 and (m+1) & m == 0
    L = m+1
    alpha = np.pi/L
    r = np.arange(1, L)
    z = (1-np.cos(r*alpha)/np.cos(alpha))/2
    z[0], z[-1] = 0.0, 1.0
    if q == 0.0 or q == 1.0:
        a = np.zeros(m)
        a[0 if q == 0.0 else -1] = 1.0
        return z, a
    assert 0 < q < 1
    D = np.sqrt(2/L)*np.sin(alpha*np.outer(r, r))
    clock = np.sqrt(2/L)*np.sin(alpha*r)
    # 2arcsin(sqrt(q)) remains accurate when q is far below machine epsilon.
    phi = 2*np.arcsin(np.sqrt(q))
    prob = np.abs(D@(clock*np.exp(1j*r*phi)))**2
    return z, prob


def clock_size(T: float, W: float, conservative=False) -> int:
    lower = max(0.0, W-1/(4*T*T)) if conservative else W
    if T*lower < 3:
        return 0
    # Largest m=2^ell-1 no larger than T W. This is precisely the theorem's
    # ideal real-arithmetic allocation; synthesis/rounding is a separate claim.
    m = 2**int(np.floor(np.log2(T*lower+1)))-1
    assert 3 <= m <= T*W+1e-12
    return m


def balanced(labels: tuple[int, ...]):
    if len(labels) == 1:
        return labels[0]
    k = len(labels)//2
    return balanced(labels[:k]), balanced(labels[k:])


def comb(labels: tuple[int, ...]):
    if len(labels) == 1:
        return labels[0]
    return labels[0], comb(labels[1:])


def leaves(tree) -> tuple[int, ...]:
    if isinstance(tree, int):
        return (tree,)
    return leaves(tree[0])+leaves(tree[1])


@dataclass
class Moments:
    mass: float
    mean: np.ndarray
    second: np.ndarray
    prep: float
    reflection: float
    min_positive: float
    min_component: float
    max_sum_error: float
    zero_mass_entries: int
    kernel_evaluations: int


def tree_moments(p: np.ndarray, tree, T: float, conservative=False) -> Moments:
    """Sum finite kernels recursively, integrating sibling laws independently.

    The second-moment cross block is an outer product of conditional sibling
    means. Thus this includes covariance from shared ancestors while avoiding
    the Cartesian product of every leaf outcome. It does not use the theorem's
    MSE recursion or substitute claimed means/variances for computed moments.
    """
    d = len(p)

    @lru_cache(maxsize=None)
    def visit(node, W: float) -> Moments:
        out = np.zeros(d)
        if W == 0:
            return Moments(1.0, out, np.zeros((d, d)), 0, 0, np.inf, 0, 0, 0, 0)
        if isinstance(node, int):
            out[node] = W
            return Moments(1.0, out, np.outer(out, out), 0, 0, W, 0, 0, 0, 0)
        ls = leaves(node)
        s = float(sum(p[i] for i in ls))
        if s == 0:
            # Such a call would represent a failure of exact face preservation.
            return Moments(1.0, out, np.zeros((d, d)), 0, 0, W, 0, W, 1, 1)
        sl = float(sum(p[i] for i in leaves(node[0])))
        q = sl/s
        m = clock_size(T, W, conservative)
        z, prob = sine_law(q, m)
        mass = 0.0
        mean = np.zeros(d)
        second = np.zeros((d, d))
        # Source-query proxies: each entered node needs one conditional
        # specimen (~s^-1/2), and m reflections (~m/s). Constants of BBHT and
        # RUS and native gates are intentionally not inferred numerically.
        prep, refl = s**-.5, m/s
        minpos, mincomp, sumerr, entered, count = np.inf, 0.0, 0.0, 0, 1
        for y, a in zip(z, prob):
            if a == 0:
                continue  # Exactly impossible endpoint outcomes only.
            wl, wr = W*y, W*(1-y)
            l = visit(node[0], float(wl))
            r = visit(node[1], float(wr))
            factor = a*l.mass*r.mass
            mass += factor
            mean += a*(l.mean*r.mass+r.mean*l.mass)
            second += a*(l.second*r.mass+r.second*l.mass
                         +np.outer(l.mean, r.mean)+np.outer(r.mean, l.mean))
            prep += a*(l.prep+r.prep)
            refl += a*(l.reflection+r.reflection)
            minpos = min(minpos, l.min_positive, r.min_positive)
            mincomp = min(mincomp, l.min_component, r.min_component, wl, wr)
            sumerr = max(sumerr, l.max_sum_error, r.max_sum_error, abs(wl+wr-W))
            entered += l.zero_mass_entries+r.zero_mass_entries
            count += l.kernel_evaluations+r.kernel_evaluations
        return Moments(mass, mean, second, prep, refl, minpos, mincomp,
                       sumerr, entered, count)

    return visit(tree, 1.0)


def finite_tree_checks() -> dict:
    vectors = [
        [0.2, 0.3, 0.5],
        [1e-12, 2e-12, 1-3e-12],
        [0.0, 0.3, 0.7],
        [0.0, 0.0, 1.0],
        [0.25]*4,
        [0.0, 1e-9, 0.4, 0.6-1e-9],
        [0.01, 0.02, 0.07, 0.3, 0.6],
        [0.0, 0.0, 0.1, 0.2, 0.7],
        [0.125]*8,
        [0.0, 0.0, 1e-10, 0.0, 0.1, 0.2, 0.3, 0.4-1e-10],
    ]
    results = []
    for p0 in vectors:
        p = np.array(p0, dtype=float)
        d = len(p)
        assert abs(sum(p)-1) < 1e-14
        Ts = [1, 3, 7, 15, 31] if d <= 5 else [3, 7, 15]
        for name, builder in [('balanced', balanced), ('comb', comb)]:
            tree = builder(tuple(range(d)))
            for T in Ts:
                for conservative in [False, True]:
                    r = tree_moments(p, tree, T, conservative)
                    mse = float(np.trace(r.second)-2*np.dot(r.mean, p)+np.dot(p, p)*r.mass)
                    assert abs(r.mass-1) < 2e-11
                    assert max(abs(r.mean-p)) < 2e-11
                    assert r.min_component >= -1e-15 and r.max_sum_error < 2e-14
                    assert r.zero_mass_entries == 0
                    assert r.min_positive*T*T >= 1-2e-12
                    assert mse >= -2e-11
                    constant = 64 if conservative else 32
                    assert mse*T*T <= constant*(d-1)+2e-9
                    assert r.prep/T <= d-1+2e-10
                    assert r.reflection/T <= d-1+2e-10
                    results.append({
                        'p': p0, 'tree': name, 'T': T,
                        'allocation': 'conservative_lower_bound_example' if conservative else 'ideal',
                        'probability_sum_error': abs(r.mass-1),
                        'maximum_mean_error': float(max(abs(r.mean-p))),
                        'mse': mse, 'T_squared_mse': mse*T*T,
                        'T_squared_min_positive': r.min_positive*T*T,
                        'prep_proxy_over_T': r.prep/T,
                        'reflection_proxy_over_T': r.reflection/T,
                        'zero_mass_entries': r.zero_mass_entries,
                        'summed_kernel_evaluations': r.kernel_evaluations,
                    })
    return {'cases': results, 'maximum_mean_error': max(x['maximum_mean_error'] for x in results),
            'maximum_scaled_mse_per_node': max(x['T_squared_mse']/(len(x['p'])-1) for x in results),
            'minimum_scaled_positive_weight': min(x['T_squared_min_positive'] for x in results)}


def direct_scalar_checks() -> dict:
    """Compute the entire clock-target experiment with complex sampler junk."""
    rng = np.random.default_rng(113)
    psi = rng.normal(size=6)+1j*rng.normal(size=6)
    psi /= np.linalg.norm(psi)
    # Three labels, each with a two-dimensional junk register. The good
    # projector combines two labels and leaves their arbitrary junk intact.
    Pi = np.diag([1, 1, 0, 0, 1, 1])
    p = float(np.vdot(psi, Pi@psi).real)
    G = (2*np.outer(psi, psi.conj())-np.eye(6))@(np.eye(6)-2*Pi)
    cases = []
    for m in [3, 7, 15, 31]:
        L = m+1
        alpha = np.pi/L
        r = np.arange(1, L)
        D = np.sqrt(2/L)*np.sin(alpha*np.outer(r, r))
        a = np.sqrt(2/L)*np.sin(alpha*r)
        histories = np.stack([a[k-1]*np.linalg.matrix_power(G, k)@psi for k in r])
        direct_prob = np.sum(abs(D@histories)**2, axis=1)
        z, phase_prob = sine_law(p, m)
        mean = float(direct_prob@z)
        var = float(direct_prob@((z-p)**2))
        kappa = (m-1)/(m+1)*np.tan(alpha)**2
        assert np.max(abs(direct_prob-phase_prob)) < 1e-12
        assert abs(mean-p) < 1e-12 and abs(var-kappa*p*(1-p)) < 1e-12
        cases.append({'m': m, 'clock_probability_error': float(max(abs(direct_prob-phase_prob))),
                      'mean_error': abs(mean-p), 'variance_formula_error': abs(var-kappa*p*(1-p)),
                      'smallest_positive_readout': float(z[1]),
                      'minimum_readout_bound': float(3/L**2)})
    return {'target_dimension': 6, 'label_count': 3, 'junk_dimension': 2,
            'good_probability': p, 'cases': cases}


def projector_encoding(Q: np.ndarray) -> np.ndarray:
    I = np.eye(len(Q))
    return np.block([[Q, I-Q], [I-Q, Q]])


def on_flag(Q: np.ndarray, flag: int, flags: int) -> np.ndarray:
    """Expand the exact projector dilation on one of several signal bits."""
    d = len(Q)
    A = np.zeros((2**flags*d, 2**flags*d), dtype=complex)
    I = np.eye(d)
    for bits in range(2**flags):
        here = slice(bits*d, (bits+1)*d)
        other = bits ^ (1 << flag)
        there = slice(other*d, (other+1)*d)
        A[here, here] = Q
        A[there, here] = I-Q
    return A


def apply_lcu(blocks: list[np.ndarray], X: np.ndarray, adjoint=False) -> np.ndarray:
    """Apply full Hadamard PREPARE/SELECT/PREPARE-dagger without dense SELECT."""
    H = np.array([[1, 1], [1, -1]])/np.sqrt(2)
    F = np.kron(H, H)
    n = blocks[0].shape[0]
    cols = X.shape[1]
    shaped = X.reshape(4, n, cols)
    prepared = np.einsum('ab,bnc->anc', F, shaped)
    selected = np.stack([(B.conj().T if adjoint else B)@prepared[j]
                         for j, B in enumerate(blocks)])
    return np.einsum('ab,bnc->anc', F, selected).reshape(4*n, cols)


def full_lcu_checks() -> dict:
    rng = np.random.default_rng(719)
    source_dimension = 3
    raw = rng.normal(size=(3, 3))+1j*rng.normal(size=(3, 3))
    U, _ = np.linalg.qr(raw)
    psi = U[:, 0]
    Pi = np.diag([1.0, 1.0, 0.0])
    v = Pi@psi
    s = float(np.vdot(v, v).real)
    R = np.eye(3)-2*np.outer(v, v.conj())/s
    # Data includes an active/inactive coherent control; both branches must
    # have the SAME success scalar s/4.
    d = 6
    V = np.block([[np.eye(3), np.zeros((3, 3))], [np.zeros((3, 3)), R]])
    QPi = np.kron(np.eye(2), Pi)
    Qpsi = np.kron(np.diag([0.0, 1.0]), np.outer(psi, psi.conj()))
    Bunit = on_flag(QPi, 0, 3)@on_flag(Qpsi, 1, 3)@on_flag(QPi, 2, 3)
    scalar_program = np.kron(np.eye(2), U.conj().T)@projector_encoding(Pi)@np.kron(np.eye(2), U)
    # Ordering: SELECT, scalar-flag/program, three B-flags, controlled data.
    scalar_unit = np.kron(scalar_program, np.eye(8*d))
    Bpad = np.kron(np.eye(2*source_dimension), Bunit)
    zero_branch = np.kron(np.array([[0, 1], [1, 0]]), np.eye(source_dimension*8*d))
    blocks = [scalar_unit, -Bpad, -Bpad, zero_branch]
    n = len(blocks[0])
    injection = np.zeros((4*n, d), dtype=complex)
    injection[:d] = np.eye(d)

    def W(X): return apply_lcu(blocks, X)
    def Wdag(X): return apply_lcu(blocks, X, adjoint=True)
    def signal_reflect(X):
        Y = -X.copy()
        Y[:d] = X[:d]
        return Y
    def amplified(X, j, adjoint=False):
        # A_j=(-A R A† R)^j A. Its top block is the standard sine amplitude.
        if not adjoint:
            Y = W(X)
            for _ in range(j):
                Y = -W(signal_reflect(Wdag(signal_reflect(Y))))
            return Y
        Y = X.copy()
        for _ in range(j):
            Y = -signal_reflect(W(signal_reflect(Wdag(Y))))
        return Wdag(Y)

    elementary_unitarity = max(float(np.linalg.norm(B.conj().T@B-np.eye(n))) for B in blocks)
    base = W(injection)
    top_error = float(np.linalg.norm(base[:d]-(s/4)*V))
    assert top_error < 2e-12 and elementary_unitarity < 2e-11
    trials = []
    for j in [0, 1, 2, 4]:
        a = np.sin((2*j+1)*np.arcsin(s/4))
        A = lambda X: amplified(X, j)
        Ad = lambda X: amplified(X, j, adjoint=True)
        first = A(injection)
        oaa_error = float(np.linalg.norm(first[:d]-a*V))
        assert oaa_error < 5e-11
        residual = first.copy()
        residual[:d] = 0
        path_errors = []
        hits = []
        for step in range(1, 11):
            Y = Ad(residual) if step % 2 else A(residual)
            K = Y[:d]
            target = np.eye(d) if step % 2 else V
            coeff = np.trace(target.conj().T@K)/d
            err = float(np.linalg.norm(K-coeff*target))
            assert err < 5e-10
            # Vectorization is the maximally entangled input/reference test.
            ref_error = float(np.linalg.norm((K-coeff*target).reshape(-1)/np.sqrt(d)))
            path_errors.append(max(err, ref_error))
            hits.append(float(np.vdot(K, K).real/d))
            residual = Y.copy()
            residual[:d] = 0
        trials.append({'amplification_steps': j, 'success_amplitude': float(a),
                       'top_block_error': oaa_error, 'maximum_halting_kraus_error': max(path_errors),
                       'first_ten_followup_hit_probabilities': hits,
                       'residual_probability_after_ten_followups': float(np.linalg.norm(residual)**2/d),
                       'infinite_trial_target_probability_formula': float(2*a*a/(1+a*a))})
    return {'source_dimension': 3, 'controlled_data_dimension': d,
            'full_lcu_hilbert_dimension': 4*n, 'subset_mass': s,
            'elementary_unitarity_error': elementary_unitarity,
            'common_scalar_controlled_top_block_error': top_error, 'trials': trials}


def composition_checks() -> dict:
    # Enumerate an actual two-outcome estimator table. Each row is independent,
    # then compare independent table products with reusing the same table.
    P = np.array([[0.8, 0.2], [0.3, 0.7]])
    T = 7
    row_laws = []
    for row in P:
        z, prob = sine_law(float(row[0]), clock_size(T, 1))
        row_laws.append([(np.array([y, 1-y]), a) for y, a in zip(z, prob) if a > 0])
    tables = [(np.vstack([r0, r1]), a*b)
              for r0, a in row_laws[0] for r1, b in row_laws[1]]
    mean = sum(w*A for A, w in tables)
    same_square = sum(w*(A@A) for A, w in tables)
    independent = sum(wa*wb*(A@B) for A, wa in tables for B, wb in tables)
    expected = P@P
    independent_error = float(np.max(abs(independent-expected)))
    reused_bias = float(np.max(abs(same_square-expected)))
    assert np.max(abs(mean-P)) < 1e-12
    assert independent_error < 1e-12 and reused_bias > 1e-3
    # Proper Brier risk: outcome J is independently drawn from the true p.
    p = P[0]
    brier = sum(a*sum(p[j]*np.sum((r-np.eye(2)[j])**2) for j in range(2))
                for r, a in row_laws[0])
    optimum = 1-np.dot(p, p)
    mse = sum(a*np.sum((r-p)**2) for r, a in row_laws[0])
    assert abs((brier-optimum)-mse) < 1e-12
    return {'T': T, 'true_transition_matrix': P.tolist(),
            'row_law_table_count': len(tables), 'independent_product_error': independent_error,
            'same_table_square': same_square.tolist(), 'true_square': expected.tolist(),
            'same_table_reuse_bias': reused_bias, 'brier_excess': float(brier-optimum),
            'probability_estimate_mse': float(mse)}


def contractive_evolution_checks() -> dict:
    """Propagate exact finite first/second moments under fresh random tables."""
    rows = []
    T = 7
    m = clock_size(T, 1.0)
    alpha = np.pi/(m+1)
    kappa = (m-1)/(m+1)*np.tan(alpha)**2
    for a in [0.0, 0.4, 0.95]:
        P = np.array([[1+a, 1-a], [1-a, 1+a]])/2
        laws = []
        for p in P[:, 0]:
            z, prob = sine_law(float(p), m)
            laws.append([(np.array([x, 1-x]), w) for x, w in zip(z, prob) if w > 0])
        tables = [(np.vstack([r, s]), wr*ws) for r, wr in laws[0] for s, ws in laws[1]]
        K = sum(w*np.kron(Q, Q) for Q, w in tables)
        v = kappa*(1-a*a)/2
        mu0 = np.array([1.0, 0.0])
        second = np.kron(mu0, mu0)
        nu = mu0.copy()
        for h in range(13):
            if h:
                second = second@K
                nu = nu@P
            mse = float(np.trace(second.reshape(2, 2))-np.dot(nu, nu))
            bound = float(kappa*(1-a**(2*h))/2)
            assert mse <= bound+2e-12 and mse >= -2e-12
            rows.append({'a': a, 'horizon': h, 'row_mse': v,
                         'distribution_vector_mse': mse, 'proved_contraction_bound': bound})
    # Same-table example stated in the page, now with an actual symmetric
    # scalar sine law rather than arbitrary mean/variance symbols.
    z, prob = sine_law(0.5, m)
    same = sum(wx*wy*(np.array([[x, 1-x], [y, 1-y]])@np.array([[x, 1-x], [y, 1-y]]))
               for x, wx in zip(z, prob) for y, wy in zip(z, prob))
    scalar_var = float(prob@((z-0.5)**2))
    formula = np.array([[0.5+scalar_var, 0.5-scalar_var],
                        [0.5-scalar_var, 0.5+scalar_var]])
    assert np.max(abs(same-formula)) < 1e-12
    return {'T': T, 'clock_m': m, 'scalar_variance_coefficient': float(kappa),
            'cases': rows, 'same_table_symmetric_formula_error': float(np.max(abs(same-formula)))}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', default=str(Path(__file__).with_name('finite-report.json')))
    args = parser.parse_args()
    report = {'status': 'passed',
              'scope': 'Deterministic finite-dimensional floating-point checks; not a proof certificate, runtime-tail simulation, finite-synthesis theorem, hardware run or external review.',
              'runtime': {'python': platform.python_version(), 'numpy': np.__version__},
              'direct_scalar_experiment': direct_scalar_checks(),
              'tree_laws': finite_tree_checks(), 'lcu_and_rus': full_lcu_checks(),
              'stochastic_composition': composition_checks(),
              'contractive_evolution': contractive_evolution_checks()}
    report['script_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    root = Path(__file__).resolve().parents[1]
    report['science_files_present_at_run'] = {
        str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
        for p in sorted((root/'science').glob('*.md'))
    }
    Path(args.output).write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({'status': report['status'], 'tree_cases': len(report['tree_laws']['cases']),
                      'maximum_mean_error': report['tree_laws']['maximum_mean_error'],
                      'maximum_scaled_mse_per_node': report['tree_laws']['maximum_scaled_mse_per_node'],
                      'controlled_lcu_top_error': report['lcu_and_rus']['common_scalar_controlled_top_block_error'],
                      'independent_product_error': report['stochastic_composition']['independent_product_error'],
                      'same_table_reuse_bias': report['stochastic_composition']['same_table_reuse_bias']}, indent=2))


if __name__ == '__main__':
    main()
