# [ABC428] ABC 428(Atcoder Beginner Contest)のA~C(A,B,C)問題をPythonで解説(復習)

#### 合計回答時間：分
# A問題
### 自分の回答
かかった時間：分
```python
S,A,B,X = map(int,input().split())

ans = 0
end = X
while end > 0:
    if end-A < 0:
        ans += end * S
        print(ans)
        exit()
    elif end-A >0 and end-(A+B) < 0:
        ans += A * S
        print(ans)
        exit()
    else:
        ans += A * S
        end -= A
        end -= B
print(ans)```

### 終了後考えた最適な回答
```python

```

# B問題
### 自分の回答
かかった時間：分
```python
# 長さ9の文字列S　＝　ovowowovo
# 長さ3の文字列tの出現回数
# 1 <= i <= 9-3+1 =7 つまりiは1から7の数
# Sのi文字目からi+2文字目までからなる部分文字列がtに一致する

N,K = map(int,input().split())
S = input()

counts = {}
for i in range(N-K+1):
    if S[i:i+K] in counts:
        counts[S[i:i+K]] += 1
    else:
        counts[S[i:i+K]] = 1

max_val = max(counts.values())
keys_of_max_val = sorted([key for key in counts if counts[key] == max_val])
print(max_val)
print(' '.join(keys_of_max_val))```

### 終了後考えた最適な回答
```python

```

# C問題
### 自分の回答
かかった時間：分
```python
# (ではじまり、)で終わる部分文字列を削除して空文字にすることができる　＝　Tを良い括弧列
# Q個のクエリがあり、処理後にSが良い括弧列か判定する
# 
def is_good(S):
    while len(S) >= 2:
        if '()' in S:
            S = S.replace('()','')
        else:
            break  
    if len(S) > 0:
        return False
    else:
        return True

Q = int(input())
S = []
for i in range(Q):
    query = input().split()
    if query[0] == '1':
        S.append(query[1])
    if query[0] == '2':
        S.pop(-1)
    flag = is_good(''.join(S))
    print('Yes' if flag else 'No')```

### 終了後考えた最適な回答
```python

```

# 次に向けてやること

# 感想

# 補足
### 関係するリンク(参考文献など)
・[今回のコンテスト](https://atcoder.jp/contests/abc428)

#### 回答の正当性は保証できません。ベストエフォート方式です。
