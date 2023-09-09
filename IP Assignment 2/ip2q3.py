#dict={"name1":{"name2":1, "name3":0, "name4":1}, "name2":{"name1":0, "name3":1, "name4":0,}, 
#"name3":{"name1":1, "name2":0, "name4":0}, "name4":{"name1":0, "name2":0, "name3":0}}

f = open('question3.txt')
l = f.read().splitlines()

students = []
signs = []
for i in l:
    if i == '':
        pass
    elif i[-1] == ':':
        i = i.replace(':','')
        students.append(i)
    else:
        if i[-1] != ':':
            signs.append(i)

new_signs = []
for i in signs:
    i = i.split(',')
    new_signs.append(i)

init = 0
signed = {}
for i in range(0,len(new_signs),len(students)-1):
    temp_dict = {}
    for j in range(len(students)-1):
        temp_dict[new_signs[i+j][0]] = int(new_signs[i+j][1])
    signed[students[init]] = temp_dict
    init += 1         

lvalues=[]
lkeys=[]
for i in signed.values():
    cnt=0
    for j in i.values():
        cnt+=j
    lvalues.append(cnt)

for i in signed.keys():
    lkeys.append(i)
x=max(lvalues)
y=min(lvalues)

a=lkeys[lvalues.index(x)]
b=lkeys[lvalues.index(y)]

maximum=[]
minimum=[]
for i in range(len(lvalues)):
    if lvalues[i]==x:
        maximum.append(lkeys[i])
    elif lvalues[i]==y:
        minimum.append(lkeys[i])

for i in minimum:
    print("minimum:", i, end="")
    print(":", y)
for j in maximum:
    print("maximum:", j, end="")
    print(":",x)