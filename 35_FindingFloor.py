a=[-6, 10, -1, 20, 15, 5]
b=-4
c=[]
for i in a:
    if i<=b:
        c.append(i)
if len(c)>=1:
    print(max(c))
else:
    print(-2147483648)