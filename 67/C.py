# 6枚のカードの山、カードの山の上から3番目のカードには3が書かれている
# それぞれのカードの数の総和をx,yとしたとき|x-y|の最小値を求めよ

N = int(input())
A = list(map(int,input().split()))

S = [0] * (N+1)

for i in range(N):
    S[i+1] = S[i] + A[i]

ans = 10**20
for i in range(1,N):
    x = S[i]
    y = S[N] - S[i]
    if abs(x-y) < ans:
        ans = abs(x-y)
print(ans)