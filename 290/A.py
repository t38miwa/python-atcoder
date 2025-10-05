N,M=map(int,input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

result=0
for i in range(len(B)):
    index=B[i]-1
    result+=A[index]

print(result)