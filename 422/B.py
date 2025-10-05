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
