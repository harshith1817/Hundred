a=[1,2,3,4,5]
b=[]
for i in range(len(a)-1,-1,-1):
    b.append(a[i])
print(b)

# #Alternate Method
# print(a[::-1])