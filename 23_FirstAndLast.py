a=[1, 3, 5, 7, 9, 11, 3, 13, 15, 3]
b=3
for i in range(len(a)):
    if a[i]==b:
        print(i)
        break
for j in range(len(a)-1,-1,-1):
    if a[j]==b:
        print(j)
        break