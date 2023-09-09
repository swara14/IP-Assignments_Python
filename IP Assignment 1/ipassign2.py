x1=0
M=int(input())
for i in range (0,200): 
    x21=120-2*x1
    x22=200-4*x1
    if x21==x22:
        print("x1=",x1, "and", end="")
        print(" x2=",x21)
        break
    else:
        x1+=1

print("Total Profit=", (M*90+M*25) + ((x1-M)*100)+(x21-M)*30)