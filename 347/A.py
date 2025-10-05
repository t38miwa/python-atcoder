N,K=map(int,input().split())

A=list(map(int,input().split()))

result=[]
for i in range(N):
    if A[i]%K==0:
        sum=A[i]//K
        result.append(str(sum))

print(' '.join(result))