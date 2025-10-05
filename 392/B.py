N,M = map(int,input().split())
A = list(map(int,input().split()))
A.sort()

result = []
for i in range(1,N+1):
    if i not in A:
        result.append(i)

print(len(result))
print(*result)