a=[1, 3, 2, 3, 4, 6, 5, 5]
b=[]
c=[]
for i in a:
    if i in b:
        c.append(i)
    else:
        b.append(i)
print(c)