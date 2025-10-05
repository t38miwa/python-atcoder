n,m=map(int,input().split())

a=list(map(int,input().split()))
b=list(map(int,input().split()))

c=sorted(a+b)

index=0
result=False
for i in range(len(c)):
    if c[i] in a:
        if index!=0 and index+1==i:
            result=True
            break
        index=i

if result:
    print('Yes')
else:
    print('No')
