N=int(input())

A=list(map(int,input().split()))

result=[]

for i in range(N-1):
    sum=A[i]*A[i+1]
    result.append(str(sum))

print(' '.join(result))