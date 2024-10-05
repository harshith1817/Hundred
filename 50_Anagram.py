a="smartinterviews"
b="viewsintersmart"
cnt=0
if len(a)!=len(b):
    print("False")
else:
    for i in a:
        if i in b:
            b=b.replace(i,"",1)
            cnt+=1
    if cnt==len(a):
        print("True")
    else:
        print("False")