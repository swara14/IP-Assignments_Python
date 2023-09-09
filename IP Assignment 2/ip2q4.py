list=["abuse", "adult", "anger", "apple", "award", "beach", "birth", "block","chain", "blood",
"drama","dream", "dress", "drink","drive", "earth", "entry", "error", "event", "faith", 
"admit", "adopt", "allow", "agree", "avoid", "blame", "chief", "chair", "child", "cream", 
"bread", "brain", "blind", "cross", "dream", "coast", "enemy", "dance", "force", "heart",
"group", "hotel", "judge", "knife", "level", "light", "metal", "money", "noise", "party"]

import random
x=random.randint(0,49)
word=list[x]

char=[]
for i in word:
    char.append(i)

for i in range(6):
    n=input("Guess a word:")
    if len(n)!=5:
        print("Enter a 5 letter word")
    elif n==word:
        print("Correct Word")
        break
    else:
        print("Incorrect Word")
        nlist=[]
        for j in n:
            nlist.append(j)

        common=[]
        for k in nlist:
            if k in char:
                common.append(k)
        s=set(common)
        print("other characters present:", end=" ")
        for a in s:
            print(a, end=" ")
        print()

        corr=[]
        for b,c in zip(nlist,char):
            if b==c:
                corr.append(b)
        print("Characters in right place:", end=" ")
        for c in corr:
            print(c, end=" ")
        print()

print("Correct word:", word)