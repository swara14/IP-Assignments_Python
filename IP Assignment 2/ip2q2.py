
#num=credits*grade

def course():

    while True:
        num=0
        cnt=0
        total_credits=0
        for j in range(len(list1)):
            print(list1[j][0], ":", list1[j][2])
            cnt+=1

            num += int(list1[j][1])* g[str(list1[j][2])]
            total_credits += int(list1[j][1])

        sgpa=num/(total_credits)
        sgpa=round(sgpa,2)
        return sgpa

def check(course_list1,g):
    if course_list1[0].isalnum():
        for i in course_list1[0]:
            if i.isalpha():
                if i.isupper():
                    pass
                else:
                    return "Improper Course Number"
        if i[-1].isdigit():
            pass
        else:
            return "Improper Course Number"
    else:
        return "Improper Course Number"
    if course_list1[1].isdigit():
        pass
    else:
        return "incorrect credit"  
    if course_list1[2] in g.keys():
        pass
    else:
        return "incorrect grade"
g={"A+":10, "A":10, "A-":9, "B":8, "B-":7, "C":6, "C-":5, "D":4, "F":2}          
list1=[]
while True:
    n=list(map(str,input("Enter course, credits, grade:").split()))
    if n==[]:
        break
    x = check(n,g)
    if x=="Improper Course Number" or x=="incorrect credit" or x=="incorrect grade":
        print(x)
        pass
    else:
        list1.append(n)
list1.sort()
print(course())