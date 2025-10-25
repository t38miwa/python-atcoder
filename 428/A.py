N,K = map(int,input().split())
A = list(map(int,input().split()))

S = [0]*(N+1)

for i in range(N):
    S[i+1] = S[i] + A[i]

ans = 0
for i in range(N-K+1):
    ans += S[i+K] - S[i]
print(ans)