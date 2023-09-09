a=int(input("angle in degrees="))
r=(a*3.14)/180
base=float(input("horizontal distance to pole="))

sinx = r - ((r**3)/6) + ((r**5)/120) 
cosx = 1 - ((r**2)/2) + ((r**4)/24) - ((r**6)/720) 

tanx = (sinx/cosx)

h= tanx * base
print("Height of the pole:",h)

hyp= cosx * base
print("distance to the tip of the pole:",hyp)