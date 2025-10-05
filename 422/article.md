# [ABC422] ABC 422(Atcoder Beginner Contest)のA~C(A,B,C)問題をPythonで解説(復習)

#### 合計回答時間：分
# A問題
### 自分の回答
かかった時間：分
```python
s = input()

i_world = int(s[0])
j_world = int(s[2])

if 1 <= j_world <= 7:
    print(f"{i_world}-{j_world+1}")
else:
    print(f"{i_world+1}-{1}")```

### 終了後考えた最適な回答
```python

```

# B問題
### 自分の回答
かかった時間：分
```python
H,W = map(int,input().split())
S = [input() for _ in range(H)]

# マスが黒く塗られているかの判定
flag = True
for i in range(H):
    for j in range(W):
        if S [i][j] == "#":
            count = 0
# もし塗られていたら上下左右のマスを調べる
            if (j < W-1) and (S[i][j+1] == "#"):
                count += 1
            if (j-1 >= 0) and (S[i][j-1] == "#"):
                count += 1
            if (i < H-1) and (S[i+1][j] == "#"):
                count += 1
            if (i-1 >= 0) and (S[i-1][j] == "#"):
                count += 1
# 黒く塗られているマスが2,4ならyesを出力
            if (count != 2) and (count != 4):
                flag = False
                break
    if not flag:
        break
# 全部のマスがこれを満たすならyesを出力
if flag: 
    print('Yes')
else:
    print('No')
```

### 終了後考えた最適な回答
```python

```

# C問題
### 自分の回答
かかった時間：分
```python
T = int(input())

result_list = []
for i in range(T):
    A,B,C = map(int,input().split())
    total = A + B + C
    result_list.append(min(A,C,total // 3))
    
for j in range(T):
    print(result_list[j])

B問題の回答に時間がかかってしまった。水分不足で脳が回らなくて変なミスをした気がする、もったいねー。C問題はgoogleで方法を検索したらそのあとはコードに落とし込めたのはよかった。

・gready法を使ったC問題を解く
・問題文通りに回答を記載するということを習慣づける
・コメントを書いて問題を整理しながら解く```

### 終了後考えた最適な回答
```python

```

# 次に向けてやること

# 感想

# 補足
### 関係するリンク(参考文献など)
・[今回のコンテスト](https://atcoder.jp/contests/abc422)

#### 回答の正当性は保証できません。ベストエフォート方式です。
