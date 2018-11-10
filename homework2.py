""" y^2=x^3+ax^2+bx+c の接線 y=Ax+B のA,Bをかえす"""
def line2(keisuu ,P ):
    a,b,c=keisuu[0],keisuu[1],keisuu[2]
    t,s=P[0],P[1]
    # 2yy'=3x^2+2ax+b
    A=(3*t**2+2*a*t+b)/(2*s)
    B=s-A*t
    return (A,B)



