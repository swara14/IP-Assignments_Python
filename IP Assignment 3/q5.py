import time
def details():
    global sep_marks
    global main_dict
    global dict
    weightage=[30,15,30,25]
    f = open('marks.txt')
    list1 = f.read().splitlines()
    #print(list1)

    list2=[]
    for i in list1:
        i=i.split(",")
        list2.append(i)
    # print(list2)

    dict={}
    sep_marks={}
    for i in list2:
        x1=round(((int(i[1])/30)*30),2)
        x2=round(((int(i[2])/15)*15),2)
        x3=round(((int(i[3])/30)*30),2)
        x4=round(((int(i[4])/25)*25),2)
        total=(x1+x2+x3+x4)
        dict[i[0]]=total

        d={}
        sep_marks[i[0]]=d
        for i in sep_marks:
            d["labs"]=x1
            d["midsem"]=x2
            d["assignments"]=x3
            d["endsem"]=x4
    # print(dict)
    # print(sep_marks)

    # grades=[80,65,50,40]
    
    policy={}
    marks_A=[]
    for k,v in dict.items():
        if v<=82 and v>=78:
            marks_A.append(v)
    policy["A"]=marks_A

    marks_B=[]
    for k,v in dict.items():
        if v<=67 and v>=63:
            marks_B.append(v)
    policy["B"]=marks_B

    marks_C=[]
    for k,v in dict.items():
        if v<=52 and v>=48:
            marks_C.append(v)
    policy["C"]=marks_C

    marks_D=[]
    for k,v in dict.items():
        if v<=42 and v>=38:
            marks_D.append(v)
    policy["D"]=marks_D
    
    for v in policy.values():
        v.sort()

    # print(policy)
    
    median={}
    for k,v in policy.items():
        if len(v)==0 or len(v)==1:
            if k=="A":
                median[k]=80
            elif k=="B":
                median[k]=65
            elif k=="C":
                median[k]=50
            elif k=="D":
                median[k]=40
        else:
            diff=[]
            for i in range(len(v)-1):
                d1=round(abs(v[i]-v[i+1]),2)
                diff.append(d1)
                m=max(diff)
                ind=diff.index(m)
            for i in range(len(v)-1):
                d2=round((abs((v[ind]+v[ind+1])/2)),2)
                median[k]=d2
    # print(median)

    med_list=[]
    for v in median.values():
        med_list.append(v)

    main_dict={}
    for k,v in dict.items():
        if v>=med_list[0]:
            main_dict[k]="A"
        elif v<med_list[0] and v>=med_list[1]:
            main_dict[k]="B"
        elif v<med_list[1] and v>=med_list[2]:
            main_dict[k]="C"   
        elif v<med_list[2] and v>=med_list[3]:
            main_dict[k]="D"
        else:
            main_dict[k]="F"
    # print(main_dict)

    count_grades={}
    c_A=0
    c_B=0
    c_C=0
    c_D=0
    c_F=0
    for v in main_dict.values():
        if v=="A":
            c_A+=1
        elif v=="B":
            c_B+=1
        elif v=="C":
            c_C+=1
        elif v=="D":
            c_D+=1
        elif v=="F":
            c_F+=1
    count_grades["A"]=c_A
    count_grades["B"]=c_B
    count_grades["C"]=c_C
    count_grades["D"]=c_D
    count_grades["F"]=c_F
    # print(count_grades)

    f=open("File Output Q5","w")
    for k,v in main_dict.items():
        f.write(k+":"+v+"\n")
    return med_list, count_grades


def student():

    roll=input("Enter roll number:")
    print()
    for k,v in sep_marks.items():
        if roll==k:
            print("Percentages of marks in each assessments:\n"+k+":"+str(v)+"\n")

    for k,v in dict.items():
        if roll==k:
            print("Total marks:\n"+k+":"+str(v)+"\n")

    for k,v in main_dict.items():
        if roll==k:
            print("Final grade:\n"+k+":"+str(v)+"\n")

print(
    "1. Generate a summary.\n"
    "2. Print grades of all students.\n"
    "3. Search for a student record.\n"
    "4. Exit"
)
med_list,count_grades=details()
count2=0
count1=0
while True:
    x=int(input("Enter a number:"))

    if x==1:
        print("Course name, Creits : IP, 4")
        print("Assessments = [(labs, 30), (midsem, 15), (assignments, 30), (endsem, 25)]")
        print("Policy:", med_list)
        print("Grading Summary:",count_grades)

    elif x==2:
        start=time.time()
        details()
        end=time.time()
        count1+=1
        print(end-start)
        print("N:",count1)
        print("Output file printed.")
    
    elif x==3:
        start=time.time()
        student()
        count2+=1
        end=time.time()
        t=(end-start)
        print("N:",count2)
        print(abs(t))

    elif x==4:
        break

details()
student()
