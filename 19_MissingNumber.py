a=[3, 5, 8, 1, 4, 7, 2]
b=sum(a)
c=0
for i in range(1,max(a)+1):
    c+=i
print(c-b)