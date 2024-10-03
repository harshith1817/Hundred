a=[4, 6, 9, 2, 5]
b,c=0,0
for i in a:
    if i%2!=0:
        b+=i
    else:
        c+=i
print(b,c)