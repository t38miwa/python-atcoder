S=list(input())

for i in range(len(S)):
    if (i+1)%2==0 and S[i]=='1':
        print('No')
        break
else:
    print('Yes')