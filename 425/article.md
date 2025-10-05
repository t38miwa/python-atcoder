# [ABC425] ABC 425(Atcoder Beginner Contest)のA~C(A,B,C)問題をPythonで解説(復習)

#### 合計回答時間：80分
# A問題
### 自分の回答
かかった時間：2分
```python
N = int(input())

result = 0
for i in range(1,N+1):
    result += (-1)**i * i**3
print(result)```

### 終了後考えた最適な回答
```python

```

# B問題
### 自分の回答
かかった時間：40分
```python
N = int(input())
A = list(map(int,input().split()))

# -1でない数字の部分はA[i] = P[i]にする
P = [0]*N
for i in range(N):
    if A[i] != -1:
        P[i] = A[i]

# リスト内に重複がある場合は即座にNoを出力
for i in range(1,N+1):
    count_P = P.count(i)
    if count_P > 1:
        print('No')
        exit()

# すでに存在する数字の部分はそのままで他のところに先頭から数字を追加
check = []
for i in range(1,N+1):
    if i not in P:
        check.append(i)

for i in range(N):
    if P[i] == 0 and len(check) >= 1:
        P[i] = check[0]
        check.pop(0)
print('Yes')
print(*P)```

### 終了後考えた最適な回答
```python

```

# C問題
### 自分の回答
かかった時間：分
```python
N,Q = map(int,input().split())
A = list(map(int,input().split()))

for i in range(Q):
    q = list(map(int,input().split()))

    # q[0]が1の場合はAの先頭の要素を末尾に移動させる操作をc回行う。
    if q[0] == 1:
        c = q[1]
        A = A[c:N]+A[0:c]
    if q[0] == 2:
        l = q[1]
        r = q[2]
        print(sum(A[c:]))```

### 終了後考えた最適な回答
```python

```

# 次に向けてやること

# 感想

# 補足
### 関係するリンク(参考文献など)
・[今回のコンテスト](https://atcoder.jp/contests/abc425)

#### 回答の正当性は保証できません。ベストエフォート方式です。
