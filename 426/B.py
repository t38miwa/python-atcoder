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
        print(k)