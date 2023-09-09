(x0,y0)=(0,0)
dist=0
list=[]

while dist>=0:
    n=int(input("Enter the distance:"))
    if 0<n<=25:
        y0+=n
    elif 25<n<=50:
        y0-=n
    elif 50<n<=75:
        x0+=n
    elif n>75:
        x0-=n
    if n==0:
        break
    list.append(n)

print("Coordinates=", end="")
print("(",x0,",",y0,")")

sum=0
for i in list:
    sum+=i
print("distance=",sum)

disp=(((x0*x0)+(y0*y0))**0.5)
print("displacement=",disp)
