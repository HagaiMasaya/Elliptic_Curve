from homework3 import kouten

def PQ(keisuu,P,Q):
    a, b, c = keisuu[0], keisuu[1], keisuu[2]
    t, s, u, v = P[0], P[1], Q[0], Q[1]
    if (t==u) and (s==-v):
        return None
    else:
        x,y=kouten(keisuu,P,Q)
        return (x,-y)

