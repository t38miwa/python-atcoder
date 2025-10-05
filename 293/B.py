N=int(input())
A=list(map(int,input().split()))
called=[]

for i in range(N):
    if i+1 in A:
        called.append(A[i])

print(len(A))
print(' '.join(str(A)))
print(' '.join(str(called)))