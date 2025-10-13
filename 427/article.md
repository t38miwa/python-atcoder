# [ABC427] ABC 427(Atcoder Beginner Contest)のA~C(A,B,C)問題をPythonで解説(復習)

#### 合計回答時間：分
# A問題
### 自分の回答
かかった時間：分
```python
S = input()

index = len(S)//2
print(S[0:index]+S[index+1:])```

### 終了後考えた最適な回答
```python

```

# B問題
### 自分の回答
かかった時間：分
```python
# AtCoder用のPythonテンプレート
# コンテスト番号: 427

# よく使う変数の初期化
ay, an, G, tr, fa = 'Yes', 'No', {}, True, False
flg, cnt, pos, rec = tr, 0, 0, []

# 入力の読み込み（必要に応じてコメントアウトを外す）
# n = int(input())
# s = input()
# a = list(map(int, input().split()))
# lst = [i+1 for i in range(n)]
N = int(input())

A = [1]
ans = 0
temp = 0
for i in range(N):
    temp = sum(A)
    ans = sum(map(int, str(temp)))
    A.append(ans)
print(temp)
# よく使う入力パターン
# a = [int(input()) for _ in range(n)]
# a = [list(map(int, input().split())) for _ in range(n)]
# a = [list(map(int, list(input()))) for _ in range(n)]
# x, y = [list(i) for i in zip(*[list(map(int, input().split())) for _ in range(n)])]

# xy = [list(map(int, input().split())) for _ in range(n)]
# x, y = [list(i) for i in zip(*xy)]

# 文字列処理
# for i in range(len(txt)):
#     ary.append(list(txt[i]))

# アルファベット変換
# A-Z：65 - 90　a-z：97 - 122　ord/chr

# デバッグ用
# print("debug:", variable_name)

# メイン処理
# ここにコードを書く

# 出力
# print(result)
```

### 終了後考えた最適な回答
```python

```

# C問題
### 自分の回答
かかった時間：分
```python
# 無向グラフとは　グラフにおいて辺に方向がないグラフのこと

# 1.グラフが二部グラフであるか判定する
# 2.二部グラフでないなら適切な辺を削除する
# 3.二部グラフであれば答えを出力する

def is_graf():
    flag = False

    return flag


N,M = map(int,input().split())

G = {}

for i in range(N):
    G[i] = set()

print(G)

for i in range(M):
    u,v = map(int,input().split())
    G[u - 1].add(v - 1)
    G[v - 1].add(u - 1)

# 二部グラフでない限りループする
while flag == false:
    ans = is_graf()
    if ans:
    else:
    
```

### 終了後考えた最適な回答
```python

```

# 次に向けてやること

# 感想

# 補足
### 関係するリンク(参考文献など)
・[今回のコンテスト](https://atcoder.jp/contests/abc427)

#### 回答の正当性は保証できません。ベストエフォート方式です。
