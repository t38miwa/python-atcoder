# 22+45+22 = 89
# 25+26+31 = 82
# 171/2 = 85

# bit全探索を使用したグループ分けを行う
# グループAの合計とグループBの合計を求める
# 大きい方の値をとる=89　89-85 = 4が最も最小の値であるかを考える

N = int(input())
K = list(map(int,input().split()))

mid_K = sum(K)/2
min_dif = sum(K)
ans = 0
for bit in range(1 << N):
    group_A = []
    for i in range(N):
        if bit & (1 << i):
            group_A.append(i)
    sum_A = 0
    for j in range(len(group_A)):
        sum_A += K[group_A[j]]
    if sum_A >= mid_K:
        if sum_A - mid_K <= min_dif:
            min_dif = sum_A - mid_K
            ans = sum_A
print(ans)