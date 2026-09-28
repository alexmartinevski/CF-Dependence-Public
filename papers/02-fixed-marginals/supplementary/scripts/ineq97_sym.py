"""Symbolic reduction of  H = (7/3) E Z^2 - (7/4) (E Z)^2 - 9 (E phi(Z))^2 >= 0  on two-point laws with E psi(Z) = 1/2 (median of X = UZ at 1).
Case A: left atom a <= 1, right atom b >= 2, q = b/(2(b-1)).  Case B: left atom 1 <= a <= 2, right atom b >= 2, q = b(2-a)/(2(b-a))."""
import sympy as sp
a, b = sp.symbols('a b', real=True)
phiL = 1 - a/2; phiR = b/2 - 1 + 1/b
# ---- Case A
q = b/(2*(b - 1))
EZ = (1 - q)*a + q*b; EZ2 = (1 - q)*a**2 + q*b**2; Ephi = (1 - q)*phiL + q*phiR
H_A = sp.together(sp.Rational(7, 3)*EZ2 - sp.Rational(7, 4)*EZ**2 - 9*Ephi**2)
coef_a2 = sp.factor(sp.expand(sp.diff(H_A, a, 2)/2))
a_star = sp.solve(sp.diff(H_A, a), a)[0]
Hmin_A = sp.factor(sp.simplify(H_A.subs(a, a_star)))
print('Case A: coefficient of a^2 =', coef_a2)
print('Case A: argmin a*(b) =', sp.factor(a_star))
print('Case A: min over a  H_min(b) =', Hmin_A)
print('   H_A(0, 3) =', sp.simplify(H_A.subs({a: 0, b: 3})), '  a*(3) =', sp.simplify(a_star.subs(b, 3)))
# ---- Case B
qB = b*(2 - a)/(2*(b - a))
phiLB = a/2 - 1 + 1/a
EZ = (1 - qB)*a + qB*b; EZ2 = (1 - qB)*a**2 + qB*b**2; Ephi = (1 - qB)*phiLB + qB*phiR
H_B = sp.factor(sp.together(sp.Rational(7, 3)*EZ2 - sp.Rational(7, 4)*EZ**2 - 9*Ephi**2))
num_B, den_B = sp.fraction(H_B)
print('Case B: H =', 'numerator/denominator with denominator', sp.factor(den_B))
print('        numerator (factored):', sp.factor(num_B))
open('ineq97_sym.txt', 'w').write('\n'.join(map(str, [coef_a2, sp.factor(a_star), Hmin_A, sp.factor(den_B), sp.factor(num_B)])))
