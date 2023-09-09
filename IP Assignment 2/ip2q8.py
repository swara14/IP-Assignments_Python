with open('question8.txt') as f:
    keyurls = []
    imp = []
    texturl = []
    a=f.read().splitlines()
    for i in a:
        split1=i.split(":")
        split2=split1[0].split(",")
        keyurls.append(split2[0])
        imp.append(float(split2[1]))
    for i in a:
        split1=i.split(":")
        split3=split1[1].split()
        a=[]
        for i in split3:
            if i[:5] in keyurls:
                a.append(i[:5])
        temp=[]
        for i in a:
            if i not in temp:
                temp.append(i)
        texturl.append(temp)
d={}
for i in range(len(keyurls)):
    d[keyurls[i]] = {
        'Init Importance': float(imp[i]), "url": (texturl[i]), "importance":0.0
    }

for k,i in d.items():
    cal=i["Init Importance"]/len(i["url"])

    for j in i['url']:
        d[j]['importance'] += cal

sort = sorted(d.items(), key=lambda x: x[1]['importance'], reverse=True)

for i in sort:
    print(i[0],":",i[1]['importance'])