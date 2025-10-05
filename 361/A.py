N,K,X=map(int,input().split())

A=list(map(int,input().split()))

result=[]

for i in range(N):
    result.append(str(A[i]))
    if i+1==K:
        result.append(str(X))

print(' '.join(result))