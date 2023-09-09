import json

def user():
    print("1. Insert a new entry\n"
    "2. Delete an entry\n"
    "3. Find all matching entries with partial name\n"
    "4. Find entry with phone number or email\n"
    "5. exit")

    with open('addressbook.txt','r') as f:
        if len(f.read().splitlines())==0:
            address_book = {}
        else:
            address_book = read()

    while True:
        x=int(input("Enter a number:"))
        if len(str(x))!=1:
            print("Please enter a choice:")
        elif x==1:
            new_address_book = new(address_book)
            address_book = {**address_book,**new_address_book}
        elif x==2:
            address_book = delete(address_book)
        elif x==3:
            partial(address_book)
        elif x==4:
            print(phone_email(address_book))
        elif x==5:
            with open('addressbook.txt',"w") as p:
                json.dump(address_book,p)
            break
        else:
            print('Invalid Input')

def read():
    with open('addressbook.txt') as f:
        data = json.load(f)
    return data

def new(address_book):
    name=input("Enter your name:")
    address=input("Enter your address:")
    phone=input("Enter your phone number:")
    email=input("Enter your email address:")
    new_address_book = {}
    d={}
    d["address"]=address
    d["phone number"]=phone
    d["email id"]=email
    new_address_book[name] = [d]
    if address_book == {}:
        address_book = new_address_book
    else:
        l = []
        for i in address_book.keys():
            if name == i:
                l.extend([d])
                l.extend(address_book[name])
        if len(l)==0:
            address_book = new_address_book
        else:
            address_book[name] = l
    return address_book

def delete(address_book):
    name=input("Enter the name of person you want to delete address of:")
    if(len(address_book[name])>1):
        address = address_book[name]
        address.remove(address[-1])
    else:
        del address_book[name]
    return address_book

def partial(address_book):
    name=input("Enter partial name to search:")
    for k in address_book.keys():
        if name.lower() in k.lower():
            print(k, address_book[k])

def phone_email(address_book):
    pe=input("Enter phone number or email address:")
    for name,info in address_book.items():
        for i in info:
            for key,value in i.items():
                if value == pe:
                    return name,i

user()