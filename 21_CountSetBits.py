a=4
b=bin(a)[2:]
c=str(b)
cnt=0
for i in c:
    if i=="1":
        cnt+=1
print(cnt)