a=[6,7,7]
a.insert(0,0)
left,right=0,0
b=[]
for i in range(1,len(a)):
    left=sum(a[:i])
    right=sum(a[i+1:])
    b.append(abs(left-right))
print(b)