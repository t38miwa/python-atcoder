# [ABC424] ABC 424(Atcoder Beginner Contest)のA~C(A,B,C)問題をPythonで解説(復習)

#### 合計回答時間：分
# A問題
### 自分の回答
かかった時間：分
```python
a,b,c = map(int,input().split())

if a == b or a == c or b == c:
    print('Yes')
else:
    print('No')```

### 終了後考えた最適な回答
```python

```

# B問題
### 自分の回答
かかった時間：分
```python
N,M,K = map(int,input().split())

result = []
count = [0]*(N+1)

for i in range(K):
    A,B = map(int,input().split())
    count[A] += 1
    if count[A] == M:
        result.append(A)

print(*result)```

### 終了後考えた最適な回答
```python

```

# C問題
### 自分の回答
かかった時間：分
```python
# (0,0)の時、高橋くんはスキルiを習得済み
# A,Bどちらかのスキルを習得済み→スキルiを習得
N = int(input())

# スキルを習得済みかどうか調べるリスト（0なら取得してない、１なら取得済み）
skill = [0] * N
for i in range(N):
    A,B = map(int,input().split())
    if A == 0 and B == 0:
        skill[i] = 1
    if skill[A-1] == 1 or skill[B-1] == 1:
        skill[i] = 1
    
count = 0
for i in range(N):
    if skill[i] == 1:
        count += 1
print(count)```

### 終了後考えた最適な回答
```python

```

# 次に向けてやること

# 感想

# 補足
### 関係するリンク(参考文献など)
・[今回のコンテスト](https://atcoder.jp/contests/abc424)

#### 回答の正当性は保証できません。ベストエフォート方式です。
