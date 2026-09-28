"""(b) exact price of F_w = w delta_0 + (1-w) U[0,1]; (c) finite d: median-split fusion (attainable for d >= 5) vs proven uniform constant."""
import numpy as np, json
from scipy.optimize import minimize, minimize_scalar
def price_w(w):
    m = (0.5 - w)/(1 - w); tau = w*m + (1 - w)*(m*m + (1 - m)**2)/2; var = (1 - w)/3 - (1 - w)**2/4; return var/tau**2
r = minimize_scalar(price_w, bounds=(0.0, 0.49), method='bounded', options={'xatol': 1e-12}); w = r.x
out = {'(b)': {'w*': round(w, 8), 'min price': round(r.fun, 8)}}; print(out, flush=True)
NU = 200000; uu = (np.arange(NU) + 0.5)/NU; xs = np.where(uu < w, 0.0, (uu - w)/(1 - w)); cs = np.concatenate([[0.0], np.cumsum(xs)])
phiw = lambda t: w + (1 - w)*(np.exp(1j*t) - 1)/(1j*t)
def D(d, t, p):
    k = min(max(int(round(p*NU)), 1), NU - 1); mm, mp = cs[k]/k, (cs[-1] - cs[k])/(NU - k)
    return abs(p*np.exp(1j*d*t*mm) + (1 - p)*np.exp(1j*d*t*mp) - phiw(t)**d)
def kappa_unif(d):
    x = np.linspace(2.0, np.pi, 100001); return float(np.max(np.sinc(2*x/d/np.pi)**d - np.cos(x)))
med = (0.5 - w)/(1 - w); tau = w*med + (1 - w)*(med**2 + (1 - med)**2)/2
rows = {}
for d in (5, 6, 8, 10, 14, 20, 30, 45, 70, 100):
    ts = np.linspace(0.8, 1.2, 801)*np.pi/(d*tau); half = np.array([D(d, t, 0.5) for t in ts]); i = int(half.argmax())
    rr = minimize(lambda z: -D(d, z[0], z[1]), (ts[i], 0.5), method='Nelder-Mead', options={'xatol': 1e-8, 'fatol': 1e-12})
    ku = kappa_unif(d)
    rows[d] = {'sup D (F_w)': round(-rr.fun, 6), 'p*': round(rr.x[1], 4), 'sup_t D(t,1/2)': round(half.max(), 6), 'kappa_d uniform': round(ku, 6),
               'difference (median split - uniform)': round(half.max() - ku, 6)}
    print(d, rows[d], flush=True)
out['(c)'] = rows; json.dump(out, open('atom_uniform_c.json', 'w'), indent=1)
