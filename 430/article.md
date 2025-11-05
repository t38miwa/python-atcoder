# [ABC430] ABC 430(Atcoder Beginner Contest)のA~C(A,B,C)問題をPythonで解説(復習)

#### 合計回答時間：分
# A問題
### 自分の回答
かかった時間：分
```python
A, B, C, D = map(int, input().split())

if C >= A and D < B:
    print("Yes")
else:
    print("No")
```

### 終了後考えた最適な回答
```python

```

# B問題
### 自分の回答
かかった時間：分
```python
# 3行3列からなるグリッド、#なら黒、.なら白
# 2行2列を取り出す方法はいくつある

N,M = map(int,input().split())
S = [list(input()) for _ in range(N)]

# resultというリストに組み合わせを保存する
results = []
for k in range(N-M+1):
    for j in range(N-M+1):
        result = []
        for i in range(M):
            result.append(S[i+k][j:j+M])
        if result not in results:
            results.append(result)
print(len(results))
```

### 終了後考えた最適な回答
```python

```

# C問題
### 自分の回答
かかった時間：分
```python
# 4分以上運転するなら2分以上休憩を取る必要がある
# 長さ11の文字列
# 1<= l <= r <= 11
# Sのlからr文字目までに含まれるaの個数が4以上
# Sのlからr文字目までに含まれるbの個数がB未満

N,A,B = map(int,input().split())
S = list(input())

for i in range(N):
    for j in range(N):
        sum_A = S[i:j].count('a')
        sum_B = S[i:j].count('b')
        if sum_A >= A and sum_B < B:
            print(i+1,j,S[i:j])```

### 終了後考えた最適な回答
```python

```

# 次に向けてやること

# 感想

# 補足
### 関係するリンク(参考文献など)
・[今回のコンテスト](https://atcoder.jp/contests/abc430)

#### 回答の正当性は保証できません。ベストエフォート方式です。
