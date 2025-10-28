# 長さ5の整数列A = [3 2 5 2 2]が与えられる
# 1<=i<j<l<=5を満たす整数の組みi,j,kであって、次の条件を満たすものの個数を求めよ
# ちょうど２種類の値が含まれる
# ３重for文で回すとTLE

#　３重for文を2重にできたとしてもO(N^2)で10^10だから厳しそう
# 入力例1の場合、[2,4]、[2,5]、[4,5]と３つペアが見つかる 
# ペア3つ×集合内のペア以外の値の数　＝3 × 2 = 6
# Aの入力例が3 2 5 2 2 2だった場合、2のペアは4C2で6ペア
# 6ペア×2 = 12
import math

N = int(input())
A = list(map(int,input().split()))

dic = {}

for i in range(N):
    if A[i] in dic:
        dic[A[i]] += 1
    else:
        dic[A[i]] = 1

ans = 0
for k,v in dic.items():
    if v > 1:
        # ペアの数を求める
        pair = math.comb(v,2)
        # 集合内のペア以外の値の数
        other = N - v
        ans += pair * other
print(ans)