from homework4 import PQ
def nP(keisuu,n,P):
    a, b, c = keisuu[0], keisuu[1], keisuu[2]
    t, s= P[0], P[1]
    if n==1:
        return P
    else:
        return nP(keisuu,n-1,PQ(keisuu,P,P))


keisuu=[0,-2,0]
P=(-1,1)
Q=(2,2)
print(nP(keisuu,499,P))

