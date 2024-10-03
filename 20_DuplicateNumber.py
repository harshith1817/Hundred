a=[5, 4, 10, 9, 21, 10]
b=[]
for i in a:
    if i not in b:
        b.append(i)
    else:
        print(i)