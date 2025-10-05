S = input()

# 入力のindexを調べる
abc = 'abcdefghijklmnopqrstuvwxyz'

result = []
for i in range(26):
    if abc[i] not in S:
        print(abc[i])
        exit()