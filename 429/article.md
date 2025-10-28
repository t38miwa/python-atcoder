# [ABC429] ABC 429(Atcoder Beginner Contest)のA~C(A,B,C)問題をPythonで解説(復習)

#### 合計回答時間：分
# A問題
### 自分の回答
かかった時間：分
```python
N,M = map(int,input().split())

for i in range(N):
    if i < M:
        print('OK')
    else:
        print('Too Many Requests')```

### 終了後考えた最適な回答
```python

```

# B問題
### 自分の回答
かかった時間：分
```python
# 長さ4の整数列A = [3 2 3 4]と整数10が与えられる
# Aの4個の要素から１個取り除くことで残りの3個の要素の和をちょうどMにできるか判定して

N,M = map(int,input().split())
A = list(map(int,input().split()))

for i in range(N):
    temp_A = A.copy()
    temp_A[i] = 0
    if sum(temp_A) == M:
        print('Yes')
        exit()
print('No')```

### 終了後考えた最適な回答
```python

```

# C問題
### 自分の回答
かかった時間：分
```python
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
print(ans)```

### 終了後考えた最適な回答
```python

```

# 次に向けてやること

# 感想

# 補足
### 関係するリンク(参考文献など)
・[今回のコンテスト](https://atcoder.jp/contests/abc429)

#### 回答の正当性は保証できません。ベストエフォート方式です。
