import math

t1=int(input("starting time="))
t2=int(input("ending time="))
t=t2-t1

v=0
n=0
while t1<=t2:
    v+=2000*math.log(140000/(140000-(2100*t1))) - (9.8*t1)
    t1+=0.25
    n+=1

vavg=v/n
d=vavg*t
print("distance=",d)
