S = list(input())

result = True
# 条件1 Tの長さが偶数
if len(S) % 2 != 0:
    result = False
# 1からT/2を満たす整数iにおいてT の (2i−1) 文字目と 2i 文字目は等しい。
for i in range(len(S)//2):
    if S[2*i] != S[2*i+1]:
        result = False
# 各文字はちょうど0か2現れる
dic = {}

for i in range(len(S)):
    if S[i] in dic:
        dic[S[i]] += 1
    else:
        dic[S[i]] = 1

for key in dic:
    if dic[key] != 2:
        result = False

print('Yes' if result else 'No')