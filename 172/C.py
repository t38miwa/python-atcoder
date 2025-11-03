# ２台の机A,Bがある
# Aには3冊の本、Bには4冊の本
# 上から２番目に積まれている本を読むのに90分かかる
# 本が残っている机を選ぶ　→ 机の最も上に積まれた本を読み終える
# これを合計時間が240分を超えないように繰り返す、この時最大何冊読める？

# 方法1
# 本を選ぶ時、最小の時間で読める本を選ぶことを繰り返す
# Aの机に最初は早く読める本がめっちゃあるけど、後からBの本がかかる時間が短い本がたくさん出てきた場合

# 方法2
# 累積和を使う
import bisect

N,M,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

sum_A = [0] * (N+1)
sum_B = [0] * (N+1)

for i in range(N):
    sum_A[i+1] = sum_A[i] + A[i]
    sum_B[i+1] = sum_B[i] + B[i]

print(sum_A,sum_B)

# Aの机の本を連続で何冊読んで、Bの机の本を連続で何冊読んだ時が制限時間内で
# 最大数の本を読めるかという答えに繋がる
cnt = 0
for i in range(N+1):
    if sum_A[i] > K:
        break
    # ソートされた配列に対し、特定の値（240-150=90）以下の要素の右端がe
    e = bisect.bisect_right(sum_B, K - sum_A[i])
    if cnt < i + e - 1:
        cnt = i + e - 1
print(cnt)