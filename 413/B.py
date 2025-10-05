N = int(input())
S = [input() for _ in range(N)]

result = []
for i in range(N):
    for j in range(N):
        if i != j:
            if S[i]+S[j] not in result:
                result.append(S[i]+S[j])
print(len(result))