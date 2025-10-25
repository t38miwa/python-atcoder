# 数直線上を3+1=4回はねるボールがある
# １回目は座標D1 = 0,2回目はD2 = D(2-1) + L(2-1)＝0+3=3ではねる
# 座標が6以下の領域でボールがはねる回数は？

N,X = map(int,input().split())
L = list(map(int,input().split()))

S = [0]*(N+1)
for i in range(N):
    S[i+1] = L[i] + S[i]

ans = 0
for i in range(len(S)):
    if S[i] <= X:
        ans += 1
print(ans)