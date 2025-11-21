# [ABC432] ABC 432(Atcoder Beginner Contest)のA~C(A,B,C)問題をPythonで解説(復習)

#### 合計回答時間：分
# A問題
### 自分の回答
かかった時間：分
```python
A,B,C = map(int,input().split())

lt = []

lt.append(A)
lt.append(B)
lt.append(C)

lt.sort(reverse=True)
new_lt = list(map(str,lt))

print(''.join(new_lt))```

### 終了後考えた最適な回答
```python

```

# B問題
### 自分の回答
かかった時間：分
```python
import itertools

X = int(input())

#　数字をリストに変換
lst = [int(d) for d in str(X)]


# intertoolsで順列全探索
all_lst = list(itertools.permutations(lst))

# 数字に戻す
ans = 10 ** 5
for i in range(len(all_lst)):
    num = int("".join(map(str, all_lst[i])))
# 先頭が0でない　かつ　値が最小なものを出力
    if len(str(num)) == len(str(X)) and num < ans:
        ans = num

print(ans)```

### 終了後考えた最適な回答
```python

```

# C問題
### 自分の回答
かかった時間：分
```python
# 小さな飴6グラム、大きな飴8グラム
# 3人の子供
# 子供2には２種類の飴を合計でちょうど10個配る
# それぞれの子供に配る飴の総重量は全て等しい

# N人全員の購入金額がちょうどぴったり一致するのなら金額をPと置いてみる
# 購入個数Aiの最小値をm,最大値をMとするとき、PはYmより大きすることはできない
# 大きい飴が整数となる条件を考える
# yiが整数である　＝　P-XAiがY-Xで割り切れる


N,X,Y = map(int,input().split())
A = list(map(int,input().split()))

def total(a,b):

    return X * a + Y * b```

### 終了後考えた最適な回答
```python

```

# 次に向けてやること

# 感想

# 補足
### 関係するリンク(参考文献など)
・[今回のコンテスト](https://atcoder.jp/contests/abc432)

#### 回答の正当性は保証できません。ベストエフォート方式です。
