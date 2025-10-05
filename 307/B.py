n=int(input())
s=[input() for i in range(n)]

result=False

for i in range(n):
    for j in range(n):
        if i != j:
            string=s[i]+s[j]
            if string==string[::-1]:
                result=True
                break
if result:
    print('Yes')
else:
    print('No')