a="hello"
b="lohel"
for i in range(1,len(a)):
    if b==a[i:]+a[:i]:
        print("yes")
        break
else:
    print("no")