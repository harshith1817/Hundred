a="aaabbb"
b={}
for i in a:
    if i in b:
        b[i]+=1
    else:
        b[i]=1
frequences=list(b.values())
for i in range(1,len(frequences)):
    if frequences[0]!=frequences[i]:
        print("False")
        break
else:
    print("True")
# print(len(set(frequences))==1)