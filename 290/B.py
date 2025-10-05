n,k=map(int,input().split())
s=list(input())

result=[]
count=0
for i in range(n):
    if s[i]=='o' and count<k:
        result.append('o')
        count+=1
    elif s[i] == 'x':
        result.append('x')
    elif s[i]=='o' and count>=k:
        result.append('x')

print(''.join(result))