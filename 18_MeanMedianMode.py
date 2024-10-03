a=[1,2,3,4,5,5,6,6]
print("Mean =",sum(a)/len(a))
if len(a)%2==0:
    print("Median =",(a[len(a)//2-1]+a[len(a)//2])/2)
else:
    print("Median =",(a[len(a)//2]))
    
frequency={}
max_count=0
mode=[]
for i in a:
    if i in frequency:
        frequency[i]+=1
    else:
        frequency[i]=1
    if frequency[i]>max_count:
        max_count=frequency[i]
        mode=[i]
    elif frequency[i]==max_count:
        mode.append(i)
print("Mode =",mode)