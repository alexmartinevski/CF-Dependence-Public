"""Rigorous finite-d comparison for F_w = w delta_0 + (1-w) U[0,1] (rational w, p).
Lower bound: attainable fusion value D(t,p) at an explicit t, evaluated with mpmath interval arithmetic (real/imag parts separately).
Attainability: both p-parts d-CM, checked exactly in rationals (M1; the atom by a weak limit).
Upper bounds: kappa_d(uniform) by grid + Lipschitz (|g'| <= 1.88) on [0, pi] and 1 + sinc(2pi/d)^d beyond; K_3(F*) = 1.087484867576..."""
import numpy as np, json
from fractions import Fraction as Fr
from mpmath import iv, mp, mpf
from scipy.optimize import minimize
iv.dps = 40; mp.dps = 40
def parts(w, p):            # exact means and CM check (rational w, p), p > w
    q = (p - w)/(1 - w); mlo = (1 - w)*q*q/2/p; mhi = (1 + q)/2
    return q, mlo, mhi
def cm_ok(w, p, d):
    q, mlo, mhi = parts(w, p); return mlo >= q/d        # lower part: nonincreasing density on [0,q] (atom as a limit); upper part U[q,1] is d-CM
def D_float(w, p, d, t):
    q, mlo, mhi = parts(float(w), float(p)); phi = float(w) + (1 - float(w))*(np.exp(1j*t) - 1)/(1j*t)
    return abs(float(p)*np.exp(1j*d*t*mlo) + (1 - float(p))*np.exp(1j*d*t*mhi) - phi**d)
def cmul(a, b): return (a[0]*b[0] - a[1]*b[1], a[0]*b[1] + a[1]*b[0])
def D_lower(w, p, d, t):    # interval lower bound for |p e^{i d t mlo} + (1-p) e^{i d t mhi} - phi(t)^d|
    q, mlo, mhi = parts(w, p); T = iv.mpf(t); W = iv.mpf(w.numerator)/w.denominator; P = iv.mpf(p.numerator)/p.denominator
    ML = iv.mpf(mlo.numerator)/mlo.denominator; MH = iv.mpf(mhi.numerator)/mhi.denominator
    phr = W + (1 - W)*iv.sin(T)/T; phi_ = (1 - W)*(1 - iv.cos(T))/T
    z = (iv.mpf(1), iv.mpf(0))
    for _ in range(d): z = cmul(z, (phr, phi_))
    re = P*iv.cos(d*T*ML) + (1 - P)*iv.cos(d*T*MH) - z[0]; im = P*iv.sin(d*T*ML) + (1 - P)*iv.sin(d*T*MH) - z[1]
    val = iv.sqrt(re*re + im*im); return mpf(val.a)
def kappa_upper(d, h=2e-6):
    x = np.arange(0, np.pi + h, h); g = np.sinc(2*x/d/np.pi)**d - np.cos(x)
    beyond = 1 + np.sinc(2/d)**d if d >= 3 else 9        # sinc(2pi/d)^d with np.sinc(y) = sin(pi y)/(pi y)
    return max(float(g.max()) + 1.88*h/2 + 1e-12, beyond)
out = {}
# ---- d = 3: maximize margin over F* subject to exact CM, rational w, p on a fine lattice
KF = 1.087484867576; best = (-1, None)
for wn in range(100, 200):
    w = Fr(wn, 1000)
    for pn in range(400, 560, 2):
        p = Fr(pn, 1000)
        if p <= w or not cm_ok(w, p, 3): continue
        ts = np.linspace(3.2, 3.8, 121); v = [D_float(w, p, 3, t) for t in ts]; i = int(np.argmax(v))
        if v[i] > best[0]: best = (v[i], (w, p, ts[i]))
w, p, t0 = best[1]
r = minimize(lambda z: -D_float(w, p, 3, z[0]), [t0], method='Nelder-Mead', options={'xatol': 1e-12, 'fatol': 1e-15}); t = round(float(r.x[0]), 8)
lb = D_lower(w, p, 3, t); q, mlo, mhi = parts(w, p)
out['d=3'] = {'w': str(w), 'p': str(p), 't': t, 'lower part CM margin (mean - q/3)': float(mlo - q/3), 'certified lower bound for K_3(F_w)': float(lb),
              'K_3(F*) (best symmetric, proven)': KF, 'sup kappa_3 over symmetric CM class': 1.0874848690, 'kappa_3 uniform (upper)': kappa_upper(3),
              'beats F*': bool(lb > KF), 'beats symmetric kappa-supremum': bool(lb > 1.0874848690), 'beats uniform': bool(lb > kappa_upper(3))}
print(json.dumps(out['d=3'], indent=1), flush=True)
# ---- d = 4 .. 60: w = 1/4, median split
rows = {}; w = Fr(1, 4); p = Fr(1, 2)
for d in list(range(4, 61)):
    tau = 7/24; ts = np.linspace(0.85, 1.15, 301)*np.pi/(d*tau); v = [D_float(w, p, d, tt) for tt in ts]; t0 = ts[int(np.argmax(v))]
    r = minimize(lambda z: -D_float(w, p, d, z[0]), [t0], method='Nelder-Mead', options={'xatol': 1e-12, 'fatol': 1e-15}); t = round(float(r.x[0]), 10)
    lb = float(D_lower(w, p, d, t)); ku = kappa_upper(d)
    rows[d] = {'t': t, 'lower bound K_d(F)': round(lb, 9), 'upper bound kappa_d(U)': round(ku, 9), 'margin': round(lb - ku, 9), 'CM': cm_ok(w, p, d)}
out['w=1/4, median split, d=4..60'] = rows
allok = all(r['margin'] > 0 and r['CM'] for r in rows.values())
print('d = 4..60 all certified:', allok, ' min margin', min(r['margin'] for r in rows.values()), ' d=4:', rows[4], flush=True)
out['all d=4..60 certified'] = allok
json.dump(out, open('cert_small_d.json', 'w'), indent=1, default=str)
