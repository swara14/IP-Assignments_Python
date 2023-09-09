n=int(input())
c=str(n)
one=["zero","one","two","three","four","five","six","seven","eight","nine"]
two1=["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
two2=["twenty","thirty","forty","fifty","sixty","Seventy","eighty","ninety"]
h="hundred"
t="thousand"
tt="ten thousand"
l="lakh"
r="crore"
if len(c)==1:
  print(one[n])

elif len(c)==2 and n<20:
  a=n%10
  print(two1[a])
elif len(c)==2 and n%10==0:
  x=n//10
  print(two2[x-2])
elif len(c)==2 and n>=20:
  a=n%10
  x=n//10
  print(two2[x-2], one[a])

elif len(c)==3 and n%100==0:
  e=n//100
  print(one[e], h)
elif len(c)==3 and n%100<=9:
  e=n//100
  f=n%100
  print(one[e], h, one[f])
elif len(c)==3 and n%100<=19:
  e=n//100
  f=n%100
  print(one[e], h, two1[f-10])
elif len(c)==3:
  e=n//100
  a=n%10
  k=(n//10)%10
  print(one[e], h, two2[k-2], one[a])

elif len(c)==4 and n%1000==0:
  m=n//1000
  print(one[m], t)
elif len(c)==4 and n%1000<=9:
  m=n//1000
  p=n%1000
  print(one[m], t, one[p])
elif len(c)==4 and n%1000<=19:
  m=n//1000
  p=n%1000
  print(one[m], t, two1[p-10])
elif len(c)==4 and n%100<=9:
  m=n//1000
  p=n%10
  q=(n//100)%10
  print(one[m], t, one[q], h, one[p])
elif len(c)==4 and n%100<=19:
  m=n//1000
  p=n%10
  q=(n//100)%10
  print(one[m], t, one[q], h, two1[p-10])
elif len(c)==4:
  m=n//1000
  q=(n//100)%10
  p=(n%100)//10
  s=n%10
  print(one[m], t, one[q], h, two2[p-2], one[s])