a="smartintsmart"
# print(a[0:3])
# print(a[-3:])
c=[]
for i in range(1,len(a)):
    if a[0:i]==a[-i:]:
        c.append(len(a[0:i]))
print(max(c))