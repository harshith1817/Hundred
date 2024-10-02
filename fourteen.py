a=[-5, 1, 5, 0, -7]
current_altitude=0
max_altitude=0
for i in range(len(a)):
    current_altitude+=a[i]
    max_altitude=max(max_altitude,current_altitude)
print(max_altitude)