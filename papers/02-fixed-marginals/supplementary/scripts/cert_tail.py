"""(i) Interval certification for d = 61..200 (F = delta0/4 + 3U/4, median split); (ii) sanity of the analytic tail bounds:
D(t_d) >= 1 + e^{-a/d} - 14.6/d^2 (a = 9pi^2/14, t_d = 24pi/(7d)) and kappa_d <= 1 + e^{-b/d} + 9.98/d^2 (b = 2pi^2/3); tail inequality for d >= 109."""
import numpy as np, json, importlib.util
spec = importlib.util.spec_from_file_location('c', 'cert_small_d.py')
src = open('cert_small_d.py').read().split('out = {}')[0]; ns = {}; exec(src, ns)
from fractions import Fraction as Fr
from scipy.optimize import minimize
w, p = Fr(1, 4), Fr(1, 2); rows = {}
for d in range(61, 201):
    tau = 7/24; ts = np.linspace(0.9, 1.1, 201)*np.pi/(d*tau); v = [ns['D_float'](w, p, d, tt) for tt in ts]; t0 = ts[int(np.argmax(v))]
    r = minimize(lambda z: -ns['D_float'](w, p, d, z[0]), [t0], method='Nelder-Mead', options={'xatol': 1e-13, 'fatol': 1e-16}); t = float(r.x[0])
    lb = float(ns['D_lower'](w, p, d, t)); ku = ns['kappa_upper'](d, h=1e-6); rows[d] = round(lb - ku, 10)
ok = all(m > 0 for m in rows.values())
print('d = 61..200 certified:', ok, ' min margin', min(rows.values()), 'at d =', min(rows, key=rows.get))
a = 9*np.pi**2/14; b = 2*np.pi**2/3; tail = {}
for d in (109, 150, 200, 500, 1000, 5000):
    td = 24*np.pi/(7*d); exactD = ns['D_float'](w, p, d, td); lbD = 1 + np.exp(-a/d) - 14.6/d**2
    x = np.linspace(2.0, np.pi, 400001); kap = float(np.max(np.sinc(2*x/d/np.pi)**d - np.cos(x))); ubK = 1 + np.exp(-b/d) + 9.98/d**2
    tail[d] = {'D(t_d) exact': round(exactD, 10), 'tail lower bound': round(lbD, 10), 'lower ok': bool(exactD >= lbD), 'kappa_d': round(kap, 10),
               'tail upper bound': round(ubK, 10), 'upper ok': bool(kap <= ubK), 'tail inequality lbD > ubK': bool(lbD > ubK),
               'check e^{-a/d}-e^{-b/d} > 24.6/d^2': bool(np.exp(-a/d) - np.exp(-b/d) > 24.6/d**2)}
    print(d, tail[d])
out = {'d=61..200 margins': rows, 'all certified 61..200': ok, 'tail checks': tail}
json.dump(out, open('cert_tail.json', 'w'), indent=1)
