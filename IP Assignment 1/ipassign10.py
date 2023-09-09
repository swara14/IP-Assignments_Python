def pol(x):
    p=x**3 - 10.5*x**2 + 34.5*x - 35
    return p

def diff(x):
    p_=3*(x**2) - 21*x + 34.5
    return p_

x0=int(input())
q = pol(x0)/diff(x0)

while abs(q)>0.0000000001:
    q = pol(x0)/diff(x0)
    x0=x0-q

print("roots of the given polynomial is:",x0)