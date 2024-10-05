a="He!!0"
has_digit=False
has_upper=False
has_lower=False
has_special=False
special_characters="!@#$%^&*()-+"
for i in a:
    if i.isdigit():
        has_digit=True
    elif i.isupper():
        has_upper=True
    elif i.islower():
        has_lower=True
    elif i in special_characters:
        has_special=True
cnt=0      
if not has_digit:
    cnt+=1
if not has_lower:
    cnt+=1
if not has_upper:
    cnt+=1
if not has_special:
    cnt+=1
length_needed=max(0,6-len(a))
print(max(cnt,length_needed))