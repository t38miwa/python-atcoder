N = int(input())
D = list(map(int,input().split()))

for i in range(N-1):
    result = D[i]
    results = []
    results.append(str(D[i]))
    for j in range(1+i,N-1):
        result += D[j]
        results.append(str(result))
    print(*results)