def star_top(z):
    n=2*z
    if z==0:
        return
    else:
        print("* "*(z) + (2*((m)-(n)))*" " + "* "*(z))
        n -= 2
        star_top((z-1))

def star_bottom(z):
    n=2*z
    if z==0:
        return
    if z==1:
        pass
    else:
        star_bottom(z-1)
        print("* "*(z) + (2*((m)-(n)))*" " + "* "*(z))
        n += 2
        
p=int(input("Enter a number:"))
m = 2*p
star_top(p)
star_bottom(p)