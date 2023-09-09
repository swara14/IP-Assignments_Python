def file(file_name):
    f = open(file_name,"r")
    list1 = f.read().splitlines()
    # print(list1)
    list2 = []
    for i in list1:
        i=i.split(" ")
        list2.append(i)
    # print(list2)

    words_list=[]
    for i in list2:
        for j in i:
            j = j.strip(':,.; ')
            words_list.append(j)
    # print(words_list)

    for i in range(len(words_list)):
        words_list[i]=words_list[i].lower()
    #print(words_list)

    final_words_list=[]
    for i in words_list:
        i=i.strip(":;,. ")
        final_words_list.append(i)
    # print(len(final_words_list))

    def factor_1():
        unique=[]
        for i in final_words_list:
            if i not in unique:
                unique.append(i)
        # print(len(unique))
        F1=len(unique)/len(final_words_list)
        return F1

    def factor_2():
        global list_count
        dict_count={}
        for i in final_words_list:
            cnt=0
            for j in final_words_list:
                if i==j:
                    cnt+=1
            dict_count[i]=cnt

        list_count=sorted(dict_count.items(), key=lambda x:x[1],reverse = True)
        # print(list_count)

        add=0
        for i in range(5):
            add+=list_count[i][1]
        # print(add)
        F2=add/len(final_words_list)
        return F2
    
    def words():
        top_five=[]
        for i in range(5):
            top_five.append(list_count[i][0])
        return top_five
    
    def random_words():
        import random
        random_five=[]
        cnt=0
        for i in final_words_list:
            random_five.append(i)
            cnt+=1
            if cnt==5:
                break
        return random_five
        #print(random_five)
        
    def factor_3():
        sen_list=[]
        for i in list1:
            i = i.split('. ')
            sen_list.extend(i)
        #print((sen_list))
        #print(len(sen_list))

        temp=[]
        for i in sen_list:
            t=i.split(" ")
            temp.append(t)
        #print(temp)

        sen_temp=[]
        for i in temp:
            if len(i)>35 or len(i)<5:
                sen_temp.append(i)

        F3=len(sen_temp)/len(sen_list)
        return F3
    
    def factor_4():
        extras=[":",",",".",";"]
        new_extras=[]
        for i in list2:
            if i[-1] in extras:
                new_extras.append(i)

        freq=0
        for i in new_extras:
            if (i[-1] and i[-2]) in extras:
                freq+=1
        #print(freq)
        F4=freq/len(list2)
        return F4

    def factor_5():
        if len(words_list)>750:
            return 1
        else:
            return 0

    F1=factor_1()
    F2=factor_2()
    F3=factor_3()
    F4=factor_4()
    F5=factor_5()
    top_5=words()
    rand=random_words()
    # print(F1,F2,F3,F4,F5)

    net_score= (4 + F1*6 + F2*6 -F3 - F4 - F5)
    return net_score,top_5,rand

with open('File Output Q3.txt','w') as f:
    while True:
        file_name=input("Enter file name:")
        if len(file_name) == 0:
            break
        f.write(file_name+"\n")
        x=file(file_name)
        f.write("Net score:"+str(x[0])+"\n")
        f.write("Top five words are:"+str(x[1])+"\n")
        f.write("Five random words are:"+str(x[2])+"\n"+"\n")
