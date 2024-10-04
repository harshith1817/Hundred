a=[100, 200, 400, 800, 1000]
b=[4, 2, 0, 6, 10, 0]
c=[]
for i in b:
    if i<=len(a):
        c.append(a[i])
    else:
        c.append(-1)
print(c)