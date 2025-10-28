# 長さ5の数列A = [1 2 4 8 16]と1以上5以下の整数3が含まれる
# この数列には長さ3の連続する部分列が5-3+1=3ある
N,K = map(int,input().split())
A = list(map(int,input().split()))

S = [0] * (N+1)

for i in range(N):
    S[i+1] = S[i] + A[i]

result = 0
for left in range(N-K+1):
    right = left + K
    result += S[right] - S[left]
print(result)