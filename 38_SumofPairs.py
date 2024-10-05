a=[10, 0]
k=20
seen=set()
found=False
for i in a:
    if k-i in seen:
        found=True
        break
    seen.add(i)
if found:
    print("True")
else:
    print("False")