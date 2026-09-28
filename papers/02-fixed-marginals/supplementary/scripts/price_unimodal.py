"""Is Var X / (E|X - med X|)^2 >= 4/3 for every unimodal law (not only symmetric)? Scan asymmetric unimodal families."""
import numpy as np, json
def ratio_from_density(xs, f):
    w = f/np.trapezoid(f, xs); F = np.concatenate([[0.0], np.cumsum((w[1:] + w[:-1])/2*np.diff(xs))]); F /= F[-1]
    mu = np.trapezoid(xs*w, xs); var = np.trapezoid((xs - mu)**2*w, xs); med = np.interp(0.5, F, xs); tau = np.trapezoid(np.abs(xs - med)*w, xs)
    return var/tau**2
xs = np.linspace(0, 1, 400001); res = {}
# linear densities f = 1 + s (1 - 2x), s in [0, 1]  (s = 0 uniform, s = 1 Beta(1,2)); unimodal (monotone)
lin = {round(s, 3): ratio_from_density(xs, 1 + s*(1 - 2*xs)) for s in (0, 0.02, 0.05, 0.1, 0.2, 0.4, 0.6, 0.8, 1.0)}
res['linear 1 + s(1-2x)'] = {k: round(v, 6) for k, v in lin.items()}
# two-step decreasing densities: h on [0,a], 1 on (a,1], h >= 1
best = (9, None)
for a in np.linspace(0.02, 0.98, 49):
    for h in np.exp(np.linspace(0, np.log(50), 60)):
        r = ratio_from_density(xs, np.where(xs <= a, h, 1.0))
        if r < best[0]: best = (r, (round(a, 3), round(h, 3)))
res['two-step decreasing: min ratio (a, h)'] = [round(best[0], 6), best[1]]
# general unimodal = mixtures of uniforms containing the mode: X = M + U*Z; take mode 0, Z two-point {-z1, z2} with weights -> densities
best2 = (9, None)
for q in np.linspace(0.02, 0.98, 49):
    for z1 in np.linspace(0.02, 1.0, 50):
        # density: q * U[-z1, 0] + (1 - q) * U[0, 1]
        xx = np.linspace(-z1, 1, 300001); f = np.where(xx < 0, q/z1, (1 - q)/1.0)
        r = ratio_from_density(xx, f)
        if r < best2[0]: best2 = (r, (round(q, 3), round(z1, 3)))
res['mode 0, q U[-z1,0] + (1-q) U[0,1]: min ratio (q, z1)'] = [round(best2[0], 6), best2[1]]
print(json.dumps(res, indent=1)); json.dump(res, open('price_unimodal.json', 'w'), indent=1)
