# 長さ8の文字列S,3個の問に答える
# 3,7が与えられ、Sの3-7の部分文字列を考える
# この文字列にACは部分文字列として何回現れる？
# 累積和配列を作り、3-7ならその配列の7-3の値がACがいくつ含まれるのかを表す

N,Q = map(int,input().split())
S = input()

AC = [0] * (N+1)
for i in range(N):
    AC[i+1] = AC[i] + (1 if S[i-1:i+1] == "AC" else 0)

for i in range(Q):
    l,r = map(int,input().split())
    print(AC[r] - AC[l])