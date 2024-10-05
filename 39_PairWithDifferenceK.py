a=[1, 20, 40, 100, 80]
k=6
cnt=False
for i in range(len(a)):
    for j in range(len(a)):
        if a[i]-a[j]==k:
            cnt=True
            break
if cnt:
    print("True")
else:
    print("False")