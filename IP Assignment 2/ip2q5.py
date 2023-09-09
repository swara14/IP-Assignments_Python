n=int(input("n:"))
cx=int(input("cx:"))
cy=int(input("cy:"))

list1=[]
for i in range(n):
    r=list(map(int,input("r:").split()))
    if len(r)==2:
        r.append(1)
        list1.append(r)
    else:
        break
#print(list1)

list2=[[cx, 0, 0], [0, cy, 0], [0, 0, 1]]
#print(list2)

result=[[0 for x in range(len(list2))] for y in range(len(list1))]
for i in range(len(list1)):
    for j in range(len(list2[0])):
        for k in range(len(list2)):
            result[i][j]+=list1[i][k]*list2[k][j]
print(result)

for i in range(len(result)):
    a=result[i][0]
    b=result[i][1]
    print("coordinates:",a,b)