a=[4, 1, 7, 4,1,4, 4]
b={}
for i in a:
    if i in b:
        b[i]+=1
    else:
        b[i]=1
pairs=0
for j in b.values():
    pairs+=j//2
print(pairs)