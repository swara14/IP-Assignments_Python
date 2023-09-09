cost=float(input("cost of laptop:"))
allowance= float(input("monthly allowance:"))
r=float(input("rate for interest:"))
sf=float(input("fraction saved:"))

savings=0
month=0
while cost>=savings:
   savings+=savings*(r/100) 
   savings += (allowance*sf)  
   month+=1
   
print(savings-cost)
print(month)
