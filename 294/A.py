N=int(input())

A=list(map(int,input().split()))

result=[]
for i in range(N):
    if A[i]%2==0:
        result.append(A[i])

print(*result)