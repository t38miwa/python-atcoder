# [ABC426] ABC 426(Atcoder Beginner Contest)のA~C(A,B,C)問題をPythonで解説(復習)

#### 合計回答時間：分
# A問題
### 自分の回答
かかった時間：分
```python
X,Y = input().split()

# indexがどちらが先か調べる
os = ["Ocelot", "Serval", "Lynx"]

x_index = 0
y_index = 0
for i in range(3):
    if X == os[i]:
        x_index = i
    if Y == os[i]:
        y_index = i

if x_index >= y_index:
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
# Sは長さ3以上、英小文字
S = list(input())

dic = {}

for i in range(len(S)):
    if S[i] not in dic:
        dic[S[i]] = 1
    else:
        dic[S[i]] += 1

for k,v in dic.items():
    if v == 1:
        print(k)```

### 終了後考えた最適な回答
```python

```

# C問題
### 自分の回答
かかった時間：分
```python
# OSのバージョンはN個ある
# PCもN台、２番目のPCのOSバージョンは２
# おそらく普通に実装するとTLEになる
# まずはTLEになってもいいから実装をする

# 普通の実装完了した
# O(Q)×O(N) = 10^11でTLE
# ①バージョンが2以下のPCを探す
# ②バージョンが2以下ならカウントに追加
# ③2以下のPCを6にアップグレード
# minという変数を作り、そこに3を入れる

N,Q = map(int,input().split())

# PCのバージョンの初期状態
PC = {}
for i in range(N):
    PC[i+1] = 1

min = 1
for i in range(Q):
    X,Y = map(int,input().split())
    # 2 6の場合、バージョン2以下のPCをバージョン6にする

    # PCのキーがminからXの値の合計を出力する
    # 累積和で実装すればいけるのだろうか？
    sum = 0
    for i in range(min,X+1):
        sum += PC[i]
        PC[i] = 0

    # sum = sum(map(PC.get, range(min,X+1)))
    
    print(sum)
    min = X
    PC[Y] += sum```

### 終了後考えた最適な回答
```python

```

# 次に向けてやること

# 感想

# 補足
### 関係するリンク(参考文献など)
・[今回のコンテスト](https://atcoder.jp/contests/abc426)

#### 回答の正当性は保証できません。ベストエフォート方式です。
