a=[1, 0, 0,1,1,1,1,1, 1, 0, 1, 1, 1, 1, 0]
maxi=0
cnt=0
for i in range(len(a)):
    if a[i]==1:
        cnt+=1
        maxi=max(maxi,cnt)
    else:
        cnt=0
print(maxi)