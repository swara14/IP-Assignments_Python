wt = [(10, 5), (20, 5), (100, 15), (40, 10), (100, 35), (100, 30)]

list1=[]
for i in l:
    string=i.strip()
    list1.append(string)

list2=[]
for i in list1:
    i = i.split(', ')
    list2.append(i)

for i in list2:
    for j in range(1,len(i)):
        i[j] = int(i[j])
print(list2)
grade=[]
grade_list = []
for i in list2:
    total = 0
    for j in range(1,len(i)):
        total+=(i[j]*wt[j-1][1])/wt[j-1][0]
    grade_list.append(total)
    if total>80:
        grade.append("A")
    elif total>70:
        grade.append("A-")
    elif total>60:
        grade.append("B")
    elif total>50:
        grade.append("B-")
    elif total>40:
        grade.append("C")
    elif total>35:
        grade.append("C-")
    elif total>30:
        grade.append("D")
    elif total<=30:
        grade.append("F")

f=open("IPgrades","w")
for i in range(len(list2)):
    f.write(list2[i][0]+","+str(grade_list[i])+","+grade[i]+'\n')