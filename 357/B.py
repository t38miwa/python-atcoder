s=input()

up_count=0
low_count=0
for i in range(len(s)):
    if s[i].isupper()==True:
        up_count+=1
    elif s[i].islower()==True:
        low_count+=1

if up_count>low_count:
    print(s.upper())
else:
    print(s.lower())