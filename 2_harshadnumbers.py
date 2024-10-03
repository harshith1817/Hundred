a=20
b=str(a)
c=[]
for i in b:
    temp=int(i)
    c.append(temp)
d=sum(c)
if a%d==0:
    print("Yes")
else:
    print("No")