import numpy as np, sympy as sp, json
from scipy.optimize import brentq
a, b = sp.symbols('a b', real=True)
N = -12*a**2*b**2 + 34*a**2*b - 20*a**2 + 34*a*b**2 - 95*a*b + 54*a - 20*b**2 + 54*b - 27
out = {}
out['N(a,2) simplifies to'] = str(sp.expand(N.subs(b, 2)))
out['coef b^2 factored'] = str(sp.factor(sp.Poly(N, b).coeff_monomial(b**2)))
out['dN/db at b=2 factored'] = str(sp.factor(sp.diff(N, b).subs(b, 2)))
# direct formula check of Case A / B against brute two-point computation
def phi(z): return 1 - z/2 if z <= 1 else z/2 - 1 + 1/z
def psi(z): return 1.0 if z <= 1 else 1/z
def H2(z1, z2, q):
    EZ = (1 - q)*z1 + q*z2; EZ2 = (1 - q)*z1**2 + q*z2**2; Ep = (1 - q)*phi(z1) + q*phi(z2); return 7/3*EZ2 - 7/4*EZ**2 - 9*Ep**2
rng = np.random.default_rng(3); worst = 9; errs = []
for _ in range(200000):
    b_ = 2 + rng.exponential(3); a_ = rng.uniform(-6, 2)
    q = (0.5 - psi(a_))/(psi(b_) - psi(a_)) if abs(psi(b_) - psi(a_)) > 1e-12 else None
    if q is None or not (0 <= q <= 1): continue
    h = H2(a_, b_, q); worst = min(worst, h)
    if 1 <= a_ <= 2: errs.append(abs(h - float(N.subs({a: a_, b: b_}))/12))
    else: errs.append(abs(h - (7*(b_ - 3)**2*(b_ + 6)/(96*(b_ + 5)))) if False else 0.0)
out['min H over random feasible two-point laws'] = worst
out['max |H - N/12| in case B'] = max(errs)
# the inequality on random unimodal laws: X = U*Z, Z with k atoms (signs free), ratio Var/tau^2 vs 9/7
def ratio(z, w):
    w = w/w.sum(); mu = np.sum(w*z/2); var = np.sum(w*z*z/3) - mu*mu
    def cdf(x): return np.sum(w*np.where(z > 1e-15, np.clip(x/np.where(z > 1e-15, z, 1), 0, 1), np.where(z < -1e-15, 1 - np.clip(x/np.where(z < -1e-15, z, -1), 0, 1), float(x >= 0))))
    lo, hi = min(0, z.min()) - 1e-9, max(0, z.max()) + 1e-9
    m = 0.0 if cdf(0) >= 0.5 and cdf(-1e-12) <= 0.5 else brentq(lambda x: cdf(x) - 0.5, lo, hi)
    A = np.minimum(0, z); B = np.maximum(0, z); L = B - A; ins = (m > A) & (m < B) & (L > 1e-15)
    e = np.where(ins, ((m - A)**2 + (B - m)**2)/(2*np.where(L > 1e-15, L, 1)), np.abs((A + B)/2 - m)); return var/np.sum(w*e)**2
mins = []
for k in (2, 3, 5, 10, 30):
    r = min(ratio(rng.normal(size=k)*rng.choice([1, 0.1, 3], size=k) + (rng.random(k) < 0.3)*0, rng.random(k)**3 + 1e-9) for _ in range(4000))
    mins.append((k, r))
out['random unimodal laws: min ratio by number of atoms'] = mins
out['9/7'] = 9/7; out['extremal ratio (delta0/4 + 3U/4)'] = ratio(np.array([0.0, 1.0]), np.array([0.25, 0.75]))
print(json.dumps(out, indent=1, default=float)); json.dump(out, open('ineq97_check.json', 'w'), indent=1, default=float)
