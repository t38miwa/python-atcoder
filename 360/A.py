S=list(input())

Rindex=0
Mindex=0
for i in range(len(S)):
    if S[i]=='R':
        Rindex=i
    elif S[i]=='M':
        Mindex=i

if Mindex>Rindex:
    print('Yes')
else:
    print('No')