N,X = map(int,input().split())
A = list(map(int,input().split()))
S = set(A)

for i in range(N):
    if A[i] - X in S:
        print('Yes')
        exit()
print('No')