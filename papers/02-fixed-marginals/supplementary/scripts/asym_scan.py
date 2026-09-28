"""(1) Price of asymmetry: sup_{t,p} D(t,p) for triangular laws on [0,1] with mode c (c = 1/2 symmetric), d = 3, 4.
(2) Large d: p*(d) and sup D(d) for an asymmetric law (Beta(1,2)); compare with the median asymptotics of Theorem 7.1."""
import numpy as np, json
from scipy.optimize import minimize
NU = 200000; uu = (np.arange(NU) + 0.5)/NU
def make_tri(c):
    Finv = lambda u: np.where(u <= c, np.sqrt(c*u), 1 - np.sqrt((1 - c)*(1 - u)))
    xs = Finv(uu); cs = np.concatenate([[0.0], np.cumsum(xs)])
    gx, gw = np.polynomial.legendre.leggauss(80)
    def phi(t):
        tot = 0j
        for lo, hi, dens in ((0.0, c, lambda x: 2*x/c), (c, 1.0, lambda x: 2*(1 - x)/(1 - c))):
            if hi - lo < 1e-12: continue
            x = (hi - lo)/2*gx + (hi + lo)/2; tot += np.sum(gw*dens(x)*np.exp(1j*t*x))*(hi - lo)/2
        return tot
    return cs, phi, xs
def make_beta12():
    xs = 1 - np.sqrt(1 - uu); cs = np.concatenate([[0.0], np.cumsum(xs)])
    gx, gw = np.polynomial.legendre.leggauss(120); x = (gx + 1)/2
    phi = lambda t: np.sum(gw*2*(1 - x)*np.exp(1j*t*x))/2
    return cs, phi, xs
def D(law, d, t, p):
    cs, phi, _ = law; k = min(max(int(round(p*NU)), 1), NU - 1); mm, mp = cs[k]/k, (cs[-1] - cs[k])/(NU - k)
    return abs(p*np.exp(1j*d*t*mm) + (1 - p)*np.exp(1j*d*t*mp) - phi(t)**d)
def supD(law, d):
    xs = law[2]; tau = np.mean(np.abs(xs - np.median(xs))); best = (-1, None)
    for t in np.linspace(0.6, 1.4, 41)*np.pi/(d*tau):
        for p in np.linspace(0.3, 0.7, 41):
            v = D(law, d, t, p)
            if v > best[0]: best = (v, (t, p))
    r = minimize(lambda z: -D(law, d, z[0], z[1]), best[1], method='Nelder-Mead', options={'xatol': 1e-7, 'fatol': 1e-11})
    return -r.fun, r.x
out = {'(1) triangular on [0,1], mode c': {}}
for c in (0.5, 0.4, 0.3, 0.2, 0.1, 0.02):
    law = make_tri(c); row = {}
    for d in (3, 4):
        v, (t, p) = supD(law, d); row[f'd={d}'] = {'sup D': round(v, 6), 'p*': round(p, 4)}
    out['(1) triangular on [0,1], mode c'][f'c={c}'] = row; print('c =', c, row, flush=True)
law = make_beta12(); xs = law[2]; med = np.median(xs); tau = np.mean(np.abs(xs - med)); var = np.var(xs); lim = np.pi**2*var/(2*tau**2)
rows = {}
for d in (3, 4, 6, 8, 12, 16, 24, 32, 48):
    v, (t, p) = supD(law, d); rows[d] = {'sup D': round(v, 7), 'p*': round(p, 5), 'd(p* - 1/2)': round(d*(p - 0.5), 4), 'd(2 - supD)': round(d*(2 - v), 5),
                                         'd^2 (2 - supD - lim/d)': round(d*d*(2 - v - lim/d), 4)}
    print('Beta(1,2) d =', d, rows[d], flush=True)
out['(2) Beta(1,2) large d'] = {'limit pi^2 Var/(2 tau^2)': round(lim, 5), 'rows': rows}
json.dump(out, open('asym_scan.json', 'w'), indent=1)
