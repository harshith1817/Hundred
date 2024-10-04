a=[5, 4, 10, 9, 21, 4, 10]
b=[]
for i in range(len(a)):
    count=0
    for j in range(len(a)):
        if a[i]==a[j]:
            count+=1
    if count==1:
        b.append(a[i])
print(b)