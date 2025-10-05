# [ABC423] ABC 423(Atcoder Beginner Contest)のA~C(A,B,C)問題をPythonで解説(復習)

#### 合計回答時間：分
# A問題
### 自分の回答
かかった時間：分
```python
X,C = map(int,input().split())

# 常に引き出し額＋手数料がX以下である必要がある

for i in range(0,X,1000):
    total = i + (i//1000)*C
    if X-C < 1000:
        print(0)
        exit(0)
    if total <= X:
        result = i

print(result)```

### 終了後考えた最適な回答
```python

```

# B問題
### 自分の回答
かかった時間：分
```python
N = int(input())
L = list(map(int,input().split()))

x = 0
y = 0
for i in range(N):
    if L[i] == 1:
        x = i
        break

for i in range(N-1,-1,-1):
    if L[i] == 1:
        y = i
        break

print(y-x)```

### 終了後考えた最適な回答
```python

```

# C問題
### 自分の回答
かかった時間：分
```python
N,R = map(int,input().split())
L = list(map(int,input().split()))

# 閉操作の後に開操作を行うことはない
# 閉操作の回数＝開く操作の回数＋始めに開いていた鍵の個数の和
if(L.count(0) == 0):
  # 何もしなくていい
  print(0)
  exit()

x = 0
y = 0
for i in range(N):
    if L[i] == 0:
        x = i
        break

for i in reversed(range(N)):
    if L[i] == 0:
        y = i
        break

mi = min(x,R)

ma = max(y+1,R)

target = L[mi:ma]

ans = target.count(1) + len(target)

print(ans)```

### 終了後考えた最適な回答
```python

```

# 次に向けてやること

# 感想

# 補足
### 関係するリンク(参考文献など)
・[今回のコンテスト](https://atcoder.jp/contests/abc423)

#### 回答の正当性は保証できません。ベストエフォート方式です。
