a=8208
b=str(a)
c=[]
for i in b:
    temp=int(i)
    temp=temp**len(b)
    c.append(temp)
if sum(c)==a:
    print("Yes")
else:
    print("No")