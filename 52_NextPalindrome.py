a=121
for i in range(a+1,a*3):
    b=str(i)
    if b==b[::-1]:
        print(b)
        break