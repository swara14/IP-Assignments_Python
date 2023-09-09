from math import e
a,b,c,d=10,1.05,1,1.06
min=1.0

def D(min):
    return (e**(a - b*min))
    

def S(min):
    return (e**(c + d*min))

def equilibrium(min):
    while D(min)>=S(min):
        min += min*0.05

    print("demand:", D(min))
    print("supply:", S(min))
    print("price",min)
equilibrium(min)