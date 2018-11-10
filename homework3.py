"""第３交点はA^2-(Pのx座標)-(Qのx座標）で与えられる"""
from homework1 import line1
from homework2 import line2
def kouten(keisuu,P,Q):
    a, b, c = keisuu[0], keisuu[1], keisuu[2]
    t, s, u, v = P[0], P[1], Q[0], Q[1]
    if not(t==u):
        A,B=line1(P,Q)
        x=A**2-t-u
        y=A*x+B
        return (x,y)
    if P==Q:
        A, B = line2(keisuu,P)
        x = A ** 2 - t - u
        y = A * x + B
        return (x, y)
    else:
        return None


