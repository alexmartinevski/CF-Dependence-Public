"""Liu-Vanduffel-Xia projection check for the mean-median deviation: gamma(u) = sign(u - 1/2).
For each inflection point xi, project gamma in L2(0,1) onto nondecreasing functions concave on (0, xi) and convex on (xi, 1).
Parametrize h = c + cumsum(derivative), derivative d_i = m + sum_{k>=i, k<j0} a_k + sum_{k<=i, k>=j0} b_k with m, a, b >= 0 (nonincreasing before xi,
nondecreasing after), c free; solve by bounded least squares. Report ||proj||^2 (the squared sup of MMD/sigma at that xi)."""
import numpy as np, json
from scipy.optimize import lsq_linear
N = 800; u = (np.arange(N) + 0.5)/N; h = 1.0/N; gamma = np.where(u < 0.5, -1.0, 1.0)
def project(xi):
    j0 = int(round(xi*N)); cols = [np.ones(N)]; lb = [-np.inf]
    L = np.tril(np.ones((N, N)))*h                    # integrates a derivative given on the grid
    D = [np.ones(N)]                                  # m
    for k in range(0, j0):                            # a_k: adds to derivative on indices <= k (nonincreasing part)
        v = np.zeros(N); v[:k + 1] = 1.0; D.append(v)
    for k in range(j0, N):                            # b_k: adds to derivative on indices >= k (nondecreasing part)
        v = np.zeros(N); v[k:] = 1.0; D.append(v)
    A = np.column_stack([np.ones(N)] + [L @ dv for dv in D]); lbs = np.array([-np.inf] + [0.0]*(len(D))); ubs = np.full(A.shape[1], np.inf)
    res = lsq_linear(A*np.sqrt(h), gamma*np.sqrt(h), bounds=(lbs, ubs), method='bvls', max_iter=5000)
    p = A @ res.x; return p, float(np.sum(p*p)*h), float(np.sum(p)*h)
out = {}
p14, n14, m14 = project(0.25)
cand = np.where(u <= 0.25, -1.0, (32*u - 17)/9)
out['xi=1/4'] = {'||proj||^2': round(n14, 6), 'mean': round(m14, 6), 'max |proj - partner candidate|': round(float(np.max(np.abs(p14 - cand))), 4), '7/9': round(7/9, 6)}
p12, n12, _ = project(0.5); out['xi=1/2'] = {'||proj||^2': round(n12, 6), 'max |proj - 3(u-1/2)|': round(float(np.max(np.abs(p12 - 3*(u - 0.5)))), 4), '3/4': 0.75}
scan = {}
for xi in [0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]:
    _, n, _ = project(xi); scan[xi] = round(n, 6)
out['||proj_xi||^2 by xi'] = scan; out['max over xi'] = max(scan.values())
print(json.dumps(out, indent=1)); json.dump(out, open('lvx_projection.json', 'w'), indent=1)
