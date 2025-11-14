# [ABC431] ABC 431(Atcoder Beginner Contest)のA~C(A,B,C)問題をPythonで解説(復習)

#### 合計回答時間：分
# A問題
### 自分の回答
かかった時間：分
```python
H,B = map(int,input().split())

if H <= B:
    print(0)
else:
    print(H-B)```

### 終了後考えた最適な回答
```python

```

# B問題
### 自分の回答
かかった時間：分
```python
# はじめロボットの重さは31
# 同時に取り付けられる部品が4つある
# 種類3の重さは65
# 4個のクエリを処理せよ
# ロボットに種類3の部品がついていない場合は取り付け、ついている場合は取り外す。
# その後にロボットの重さを出力する

X = int(input())
N = int(input())
W = list(map(int,input().split()))
Q = int(input())

have = []
ans = X
for i in range(Q):
    P = int(input())
    if P in have:
        have.remove(P)
        ans -= W[P-1]
        print(ans)
    else:
        have.append(P)
        ans += W[P-1]
        print(ans)```

### 終了後考えた最適な回答
```python

```

# C問題
### 自分の回答
かかった時間：分
```python
# 高橋くん頭パーツ6個、体パーツ6個持ってる
# ２番目の頭パーツは7,２番目の体パーツは8
# 倒れないロボットを合計3体作りたい
# 二重for文回した時点でTLE

# H<Bとなるような組み合わせをK個作りたい
# Hの3つ目が2,つまり、Bに2以上の値が3以上あればYes
import bisect

N,M,K = map(int,input().split())
H = list(map(int,input().split()))
B = list(map(int,input().split()))

sh = sorted(H)
sb = sorted(B)
ans_h = sh[:K]
ans_b = sb[M-K:]

for i in range(K):
    if ans_h[i] > ans_b[i]:
        print('No')
        exit()
print('Yes')```

### 終了後考えた最適な回答
```python

```

# 次に向けてやること

# 感想

# 補足
### 関係するリンク(参考文献など)
・[今回のコンテスト](https://atcoder.jp/contests/abc431)

#### 回答の正当性は保証できません。ベストエフォート方式です。
