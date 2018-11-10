""" 接線のA,B を与える関数"""
def line1( P , Q ) :
    t,s,u,v=P[0],P[1],Q[0],Q[1]
    if t == u:
        return None
    else:
        A = (v - s) / (u - t)
        B = s - A * t
        return (A, B)



