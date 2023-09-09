n=int(input())
c=str(n)
one=["zero","one","two","three","four","five","six","seven","eight","nine"]
two1=["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
two2=["twenty","thirty","fourty","fifty","sixty","Seventy","eighty","ninety"]
if len(c)==1:
    print(one[n])
elif len(c)==2 and n<20:
    a=n%10
    print(two1[a])
elif len(c)==2 and n%10==0:
    x=n//10
    print(two2[x-2])
elif len(c)==2 and n>=20:
    c=n%10
    d=n//10
    print(two2[d-2]+" ", end="")
    print(one[c])