"""d = 3: F_w = w delta0 + (1-w) U[0,1]. Attainable fusions: both p-parts must be 3-CM. Lower part (p >= w): (w/p) delta0 + U-part on [0, q_p],
q_p = (p - w)/(1 - w); it has a nonincreasing density (atom as a limit) -> 3-CM iff mean >= q_p/3 (M1). Upper part: U[q_p, 1] -> CM.
(For p < w the lower part is an atom -> CM; the upper part (atom + uniform) is nonincreasing on [0,1] after the atom -> M1 with shift.)"""
import numpy as np, json
from scipy.optimize import minimize_scalar
def parts(w, p):
    if p <= w:
        mlo = 0.0; lo_ok = True
        # upper part: ((w-p)/(1-p)) delta0 + ((1-w)/(1-p)) U[0,1]: nonincreasing on [0,1]; mean = (1-w)/(2(1-p)); M1: mean >= 1/3
        mhi = (1 - w)/(2*(1 - p)); hi_ok = mhi >= 1/3 - 1e-15
    else:
        q = (p - w)/(1 - w); mlo = ((1 - w)*q*q/2)/p; lo_ok = mlo >= q/3 - 1e-15
        mhi = (1 + q)/2; hi_ok = True
    return mlo, mhi, lo_ok and hi_ok
def phi(w, t): return w + (1 - w)*(np.exp(1j*t) - 1)/(1j*t)
def D(w, d, t, p):
    mlo, mhi, ok = parts(w, p); return abs(p*np.exp(1j*d*t*mlo) + (1 - p)*np.exp(1j*d*t*mhi) - phi(w, t)**d), ok
d = 3; TG = np.linspace(2.0, 12.0, 3001); best_all = (-1, None)
rows = {}
for w in np.round(np.linspace(0.05, 0.3, 26), 4):
    bw = (-1, None)
    for p in np.linspace(0.02, 0.98, 193):
        mlo, mhi, ok = parts(w, p)
        if not ok: continue
        vals = np.abs(p*np.exp(1j*d*TG*mlo) + (1 - p)*np.exp(1j*d*TG*mhi) - phi(w, TG)**d); i = int(vals.argmax())
        if vals[i] > bw[0]: bw = (vals[i], (TG[i], p))
    t0, p0 = bw[1]
    r = minimize_scalar(lambda t: -D(w, d, t, p0)[0], bounds=(t0 - 0.01, t0 + 0.01), method='bounded', options={'xatol': 1e-10})
    rows[float(w)] = {'best attainable fusion': round(-r.fun, 7), 'p': round(p0, 4), 't': round(r.x, 5)}
    if -r.fun > best_all[0]: best_all = (-r.fun, (float(w), p0, r.x))
for w, v in rows.items(): print(w, v)
out = {'d=3 attainable fusions for F_w': rows, 'best': [round(best_all[0], 8), best_all[1]], 'uniform kappa_3': 1.0849633414,
       'sup kappa_3 over symmetric unimodal 3-CM class (F* ~)': 1.0874848690}
# refine w near the best
wb = best_all[1][0]
def best_for_w(w):
    b = -1
    for p in np.linspace(max(0.02, w - 0.2), 0.98, 400):
        mlo, mhi, ok = parts(w, p)
        if not ok: continue
        vals = np.abs(p*np.exp(1j*d*TG*mlo) + (1 - p)*np.exp(1j*d*TG*mhi) - phi(w, TG)**d); b = max(b, vals.max())
    return b
ws = np.linspace(max(0.01, wb - 0.02), wb + 0.02, 41); vb = [best_for_w(w) for w in ws]; k = int(np.argmax(vb))
out['refined'] = {'w': round(ws[k], 5), 'value (grid in t)': round(vb[k], 7), 'exceeds symmetric supremum 1.0874848690': bool(vb[k] > 1.0874848690)}
print(json.dumps({kk: out[kk] for kk in ('best', 'refined')}, indent=1)); json.dump(out, open('d3_asym.json', 'w'), indent=1, default=float)
