"""Is 9/7 the infimum of Var/(E|X-med|)^2 over unimodal laws? X = U*Z (mode 0), Z discrete with k atoms (signs free).
Vectorized exact formulas; plus d = 3, 4 check for F = delta0/4 + 3U[0,1]/4 (median split) and small-d optimum over w."""
import numpy as np, json
from scipy.optimize import minimize, brentq
def price(z, q):
    q = np.abs(q); q = q/q.sum(); mu = np.sum(q*z/2); var = np.sum(q*z*z/3) - mu*mu
    def cdf(x):
        pos = z > 1e-12; neg = z < -1e-12; zero = ~(pos | neg)
        c = np.where(pos, np.clip(x/np.where(pos, z, 1), 0, 1), 0.0) + np.where(neg, 1 - np.clip(x/np.where(neg, z, -1), 0, 1), 0.0) + np.where(zero, float(x >= 0), 0.0)
        return np.sum(q*c)
    lo, hi = min(0.0, z.min()), max(0.0, z.max()); m = brentq(lambda x: cdf(x) - 0.5, lo - 1e-9, hi + 1e-9) if cdf(lo) < 0.5 < cdf(hi) else (0.0 if cdf(0) >= 0.5 else hi)
    a = np.minimum(0, z); b = np.maximum(0, z); L = b - a
    inside = (m > a) & (m < b) & (L > 1e-12)
    e = np.where(inside, ((m - a)**2 + (b - m)**2)/(2*np.where(L > 1e-12, L, 1)), np.abs((a + b)/2 - m))
    return var/np.sum(q*e)**2
rng = np.random.default_rng(1); best = {}
for k in (2, 3, 4):
    bk = (9, None)
    for trial in range(120):
        x0 = np.concatenate([rng.uniform(-1, 1, k), rng.uniform(0.05, 1, k)])
        f = lambda v: price(v[:k], v[k:]) if np.all(np.abs(v[k:]) > 1e-7) and np.ptp(np.concatenate([v[:k], [0]])) > 1e-6 else 9.0
        res = minimize(f, x0, method='Nelder-Mead', options={'maxiter': 3000, 'xatol': 1e-10, 'fatol': 1e-13})
        if res.fun < bk[0]: bk = (res.fun, np.round(res.x[:k], 4).tolist(), np.round(np.abs(res.x[k:])/np.abs(res.x[k:]).sum(), 4).tolist())
    best[k] = {'min price': round(bk[0], 9), 'atoms z': bk[1], 'probs': bk[2]}; print(k, best[k], flush=True)
out = {'9/7': 9/7, 'min over k atoms': best}
# small d for F_w: median split value vs uniform
NU = 200000; uu = (np.arange(NU) + 0.5)/NU
def fam(w):
    xs = np.where(uu < w, 0.0, (uu - w)/(1 - w)); cs = np.concatenate([[0.0], np.cumsum(xs)])
    phi = lambda t: w + (1 - w)*(np.exp(1j*t) - 1)/(1j*t); return cs, phi
def Dv(cs, phi, d, t, p):
    k = min(max(int(round(p*NU)), 1), NU - 1); mm, mp = cs[k]/k, (cs[-1] - cs[k])/(NU - k)
    return abs(p*np.exp(1j*d*t*mm) + (1 - p)*np.exp(1j*d*t*mp) - phi(t)**d)
ku = {3: 1.0849633414, 4: 1.1907222653}; small = {}
for d in (3, 4):
    rows = {}
    for w in (0.1, 0.15, 0.2, 0.25, 0.3, 0.35):
        cs, phi = fam(w); m = (0.5 - w)/(1 - w); lowmean = ((1 - w)*m*m/2)/0.5
        cm_ok = bool(lowmean >= m/d - 1e-12)       # M1 for the lower half: mean >= b/d
        vals = [(Dv(cs, phi, d, t, 0.5), t) for t in np.linspace(1.0, 12.0, 2201)]
        v, t = max(vals); rows[w] = {'median-split sup_t D': round(v, 6), 'lower half d-CM (M1)': cm_ok, 'beats uniform kappa_d': bool(v > ku[d] and cm_ok)}
    small[d] = rows; print(d, rows, flush=True)
out['small d, median split'] = small; json.dump(out, open('price_inf.json', 'w'), indent=1)
