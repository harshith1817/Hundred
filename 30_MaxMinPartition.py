a=[7, 1, 14, 16, 30, 4]
a.sort()
mini=max(a)
for i in range(1,len(a)):
    mini=min(mini,a[i]-a[i-1])
print(mini)