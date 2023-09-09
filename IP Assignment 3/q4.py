import time
f = open('marks_file.txt')
list1 = f.read().splitlines()

list2=[]
for i in list1:
    i=i.split(", ")
    list2.append(i)

class Course:
    def __init__(self):
        self.dict = {}
        self.sep_marks={}

    def marks(self):
        for i in list2:
            x1=round(((int(i[1])/100)*30),2)
            x2=round(((int(i[2])/100)*15),2)
            x3=round(((int(i[3])/100)*30),2)
            x4=round(((int(i[4])/100)*25),2)
            total=(x1+x2+x3+x4)
            self.dict[i[0]]=total
            d={}
            self.sep_marks[i[0]]=d
            for i in self.sep_marks:
                d["labs"]=x1
                d["midsem"]=x2
                d["assignments"]=x3
                d["endsem"]=x4
        return self.sep_marks,self.dict
    
    def new_policy(self):
        global policy
        policy={}
        marks_A=[]
        for k,v in self.dict.items():
            if v<=82 and v>=78:
                marks_A.append(v)
        policy["A"]=marks_A

        marks_B=[]
        for k,v in self.dict.items():
            if v<=67 and v>=63:
                marks_B.append(v)
        policy["B"]=marks_B

        marks_C=[]
        for k,v in self.dict.items():
            if v<=52 and v>=48:
                marks_C.append(v)
        policy["C"]=marks_C

        marks_D=[]
        for k,v in self.dict.items():
            if v<=42 and v>=38:
                marks_D.append(v)
        policy["D"]=marks_D

        for v in policy.values():
            v.sort()

    def median(self):
        global med_list
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
        med_list=[]
        for v in median.values():
            med_list.append(v)

class Student:
    def __init__(self, student,sep_marks,dictionary):
        self.students=student
        self.sep_marks = sep_marks
        self.dictionary = dictionary
        self.main_dict={}
        self.count_grades = {}

    def final_grades(self):
        for k,v in self.dictionary.items():
            if v>=med_list[0]:
                self.main_dict[k]="A"
            elif v<med_list[0] and v>=med_list[1]:
                self.main_dict[k]="B"
            elif v<med_list[1] and v>=med_list[2]:
                self.main_dict[k]="C"   
            elif v<med_list[2] and v>=med_list[3]:
                self.main_dict[k]="D"
            else:
                self.main_dict[k]="F"
        return self.main_dict

    def student(self):

        roll=input("Enter roll number:")
        print()
        for k,v in self.sep_marks.items():
            if roll==k:
                print("Percentages of marks in each assessments:\n"+k+":"+str(v)+"\n")

        for k,v in self.students.items():
            if roll==k:
                print("Total marks:\n"+k+":"+str(v)+"\n")

        for k,v in self.main_dict.items():
            if roll==k:
                print("Final grade:\n"+k+":"+str(v)+"\n")

    def grades(self):
        c_A=0
        c_B=0
        c_C=0
        c_D=0
        c_F=0
        for v in self.main_dict.values():
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
        self.count_grades["A"]=c_A
        self.count_grades["B"]=c_B
        self.count_grades["C"]=c_C
        self.count_grades["D"]=c_D
        self.count_grades["F"]=c_F
        return self.count_grades


def main():
    x = Course()
    sep_marks,dictionary = x.marks()
    x.new_policy()
    x.median()
    n = int(input())
    y = Student(med_list,sep_marks,dictionary)
    if n == 1:
        pass
    elif n == 2:
        f=open("File Output Q5","w")
        for k,v in y.final_grades().items():
            f.write(k+":"+v+"\n")
        f.close()
    elif n == 3:
        pass

main()