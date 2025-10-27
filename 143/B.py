# ３個のたこ焼きが振舞われる
# 2個目のたこ焼きの美味しさは1
# おいしさがx,yであるたこ焼きを一緒に食べると体力がx*y回復する
# ３このたこ焼きから２こを

N = int(input())
D = list(map(int,input().split()))

S = [0] * (N+1)
for i in range(N):
    S[i+1] = D[i] + S[i]

ans = 0
for i in range(N-1):
    #3 * (6-3)
    ans += D[i] * (S[N] - S[i + 1])
print(ans)