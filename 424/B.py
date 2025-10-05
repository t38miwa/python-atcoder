N,M,K = map(int,input().split())

result = []
count = [0]*(N+1)

for i in range(K):
    A,B = map(int,input().split())
    count[A] += 1
    if count[A] == M:
        result.append(A)

print(*result)