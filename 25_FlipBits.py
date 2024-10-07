a=549
b=24
c=bin(a)[2:]
d=bin(b)[2:]
e=str(c)
f=str(d)
g="0"
if len(e)!=len(f):
    if len(e)>len(f):
        for _ in range(len(e)-len(f)):
            f=g+f
    else:
        for _ in range(len(f)-len(e)):
            e=e+g   
cnt=0
for i in range(len(e)):
    if e[i]!=f[i]:
        cnt+=1
print(cnt)