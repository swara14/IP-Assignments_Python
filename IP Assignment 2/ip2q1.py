menu = [("Samosa", 15), ("Idli", 30), ("Maggie", 50), ("Dosa", 70), ("Tea", 10), ("Coffee", 20), ("Sandwich", 35), ("ColdDrink", 25)]
x=[1,2,3,4,5,6,7,8,9]
for i in range(len(menu)):
    print(x[i], menu[i][0], ":", "Rs.", menu[i][1])

list1=[]
while True:
    n=list(map(int,input("Enter your order:").split()))
    if n == []:
        print()
        for j in range(len(list1)):
            print(menu[list1[j][0]-1][0], list1[j][1], "Rs.", menu[list1[j][0]-1][1]*list1[j][1])
        break
    else:
        list1.append(n)
        

total=0
cnt=0
for j in range(len(list1)):
    total += ( (list1[j][1]) * (menu[(list1[j][0])-1][1]) )
    cnt+=1

print()
print("Total:",cnt, "items", "Rs.", total)