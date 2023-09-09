f = open('sorted_data.txt')
list1 = f.read().splitlines()
print(list1)
list2=[]
for i in list1:
    split1=i.split(", ")
    list2.append(split1)
list2.remove(list2[0])
# print(list2)
#print()

main_dict={}
for i in list2:
    if i[0] not in main_dict:
        main_dict[i[0]]={}
#print(main_dict)
#print()

for i in list2:
    d={}
    temp_list=[]
    for k,v in main_dict.items():
        if i[0]==k:
            d["crossing"]=i[1]
            d["gate"]=i[2]
            d["time"]=i[3]
            #print(d)
            temp_list.extend(v)
            temp_list.append(d)
    main_dict[i[0]]=temp_list
# print(main_dict)

# #taking input from user
print( "1. Find details by name\n"
"2. Find details by start and end time\n"
"3. Find details by gate number\n" 
"4. Exit")

def part1():
    nm=input("Enter a name:")
    tm=input("Enter current time:")

    temp_time=[]
    try:
        for i in main_dict[nm]:
            if i["time"]<=tm:
                #print(i)
                temp_time.append(i)
        #print(temp_time)

        ind=((len(temp_time))-1)
        if temp_time[ind]["crossing"]=="ENTER":
            return (nm, "is in campus.")
        else:
            return (nm,"is not in campus at the current time.")
    except:
        if i["time"]>=tm:
            return (nm,"did not enter or exit the campus.")

def part2(f):
    start_tm=input("Enter start time:")
    end_tm=input("Enter end time:")
    for k,v in main_dict.items():
        for i in v:
            if start_tm<=i["time"]<=end_tm:
                f.write(k+', '+i['crossing']+', '+i['gate']+', '+i['time']+'\n')

def part3():
    gt=input("Enter gate number:")

    count1_enter=[]
    count3_enter=[]
    count5_enter=[]
    for i in list2:
        if i[2]=='1' and i[1]=="ENTER":
            count1_enter.append(i)    
        elif i[2]=='3' and i[1]=="ENTER":
            count3_enter.append(i)
        elif i[2]=='5' and i[1]=="ENTER":
            count5_enter.append(i)
    if gt=="1":
        print("Number of students entered gate1:",len(count1_enter))
    if gt=="3":
        print("Number of students entered gate3:",len(count3_enter))
    if gt=="5":
        print("Number of students entered gate5:",len(count5_enter))

    count1_exit=[]
    count3_exit=[]
    count5_exit=[]
    for i in list2:
        if i[2]=='1' and i[1]=="EXIT":
            count1_exit.append(i)    
        elif i[2]=='3' and i[1]=="EXIT":
            count3_exit.append(i)
        elif i[2]=='5' and i[1]=="EXIT":
            count5_exit.append(i)
    if gt=="1":
        print("Number of students exited gate1:",len(count1_exit))
    if gt=="3":
        print("Number of students exited gate3:",len(count3_exit))
    if gt=="5":
        print("Number of students exited gate5:",len(count5_exit))

with open("File Output Q2.txt","w") as f:
    while True:
        x=int(input("Enter a number:"))
        if x==1:
            p=part1()
            f.write(str(p[0])+str(p[1])+"\n"+"\n")
        elif x==2:
            part2(f)
        elif x==3:
            part3()
        elif x==4:
            break