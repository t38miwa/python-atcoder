S = [input() for _ in range(8)]

# 駒を見つけたとき、その上下左右のマスを@に変える
flag = [1] * 8
for i in range(8):
    result = False
    for j in range(8):
        if S[i][j] == "#":
            result = True
            flag[j] = 0
    if result:
        S[i] = "@"*8

# もう一度for文を回して.のマスの数を計算する
count = 0
for i in range(8):
    for j in range(8):
        if S[i][j] == "." and flag[j] == 1:
            count += 1
print(count)