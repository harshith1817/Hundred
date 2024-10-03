a=[120, 0, -9, 89, 68, -982, 91, -54, -12, -139]
b,c,d=0,0,0
for i in a:
    if i==0:
        b+=1
    elif i>0:
        c+=1
    else:
        d+=1
print(b,c,d)