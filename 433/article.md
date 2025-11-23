# [ABC433] ABC 433(Atcoder Beginner Contest)のA~C(A,B,C)問題をPythonで解説(復習)

#### 合計回答時間：分
# A問題
### 自分の回答
かかった時間：分
```python
X,Y,Z = map(int,input().split())

for i in range(100):
    if (X + i) == Z * (Y + i):
        print('Yes')
        exit()

print('No')```

### 終了後考えた最適な回答
```python

```

# B問題
### 自分の回答
かかった時間：分
```python
# 4人の人が並んでいる
# 左から2人目の人を人2と呼ぶ、この人の身長は3

# 計算量は考慮しなくてよさそう
# 自分より左にいる人のリストを毎度作成する
# リストに対してfor文を回し、リスト内の身長-自分の身長の値が0以上かつ最も小さいindexを求める

N = int(input())
A = list(map(int,input().split()))

for i in range(N):
    left_lst = A[:i]
    ## 一つ目は必ず-1
    if len(left_lst) == 0:
        print(-1)
        continue
    ans = 0
    for j in range(len(left_lst)):
        height_diff = left_lst[j] - A[i]
        if height_diff > 0:
            ans = j+1
    if ans == 0:
        print(-1)
    else:
        print(ans)
```

### 終了後考えた最適な回答
```python

```

# C問題
### 自分の回答
かかった時間：分
```python
s = input()
n = len(s)
ans = 0
for i in range(n - 1):
    if int(s[i]) + 1 != int(s[i + 1]):
        continue
    j = i
    while j != -1 and s[j] == s[i]:
        j -= 1
    k = i + 1
    while k != n and s[k] == s[i + 1]:
        k += 1
    ans += min(i - j, k - i - 1)
print(ans)```

### 終了後考えた最適な回答
```python

```

# 次に向けてやること

# 感想

# 補足
### 関係するリンク(参考文献など)
・[今回のコンテスト](https://atcoder.jp/contests/abc433)

#### 回答の正当性は保証できません。ベストエフォート方式です。
