list=["abuse", "adult", "anger", "apple", "award", "beach", "birth", "block","chain", "blood",
"drama","dream", "dress", "drink","drive", "earth", "entry", "error", "event", "faith", 
"admit", "adopt", "allow", "agree", "avoid", "blame", "chief", "chair", "child", "cream", 
"bread", "brain", "blind", "cross", "dream", "coast", "enemy", "dance", "force", "heart",
"group", "hotel", "judge", "knife", "level", "light", "metal", "money", "noise", "party"]

import requests 
import json
import random
c = 0

def api(a):
    app_id  = "ccc28cad"
    app_key  = "5000c84ad7d2c2776572066bea7cc792"
    endpoint = "entries"
    language_code = "en-us"
    url = "https://od-api.oxforddictionaries.com/api/v2/" + endpoint + "/" + language_code + "/" + a.lower()
    r = requests.get(url, headers = {"app_id": app_id, "app_key": app_key})
    if a in r.text:
        return True
    else:
        return False

x=random.randint(0,49)
word=list[x]

char=[]
for i in word:
    char.append(i)

for i in range(6):
    n=input("Guess a word:")
    c += 1
    s = api(x)
    if s == True:
        print('Word in Dictionary')
            
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
    else:
        print('Word not in dictionary')

print("Correct word:", word)