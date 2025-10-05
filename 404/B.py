# グリッドSのマスの色を変更する
# Sを90度右回転
# 回転優先
# 回転はもともとのSと合わせて４パターンある
N = int(input())
S = [list(input()) for _ in range(N)]
T = [list(input()) for _ in range(N)]

# 色を変更する必要がある回数を返す関数
def dif_count(S,N):
    dif_count = 0
    for i in range(N):
        for j in range(N):
            if S[i][j] != T[i][j]:
                dif_count += 1
    return dif_count

def right_rot90(S):
  return list(zip(*S[::-1]))

print(right_rot90(S))

# 右回転させる
def right_turn(S,N):
    rotated_S = [list("@"*N) for _ in range(N)]
    for i in range(N):
            for j in range(N):
                #(0,0)から(0,3)までを変えてみる
                rotated_S[i][j] = S[N-1-j][i]
    return rotated_S

# 4パターンの中で最もdif_countが少ないパターンを導く。回転回数＋dif_countが答え
# 回転数+
result_count = dif_count(S,N)
turn_count = 0
for i in range(N-1):
    S = right_turn(S,N)
    turn_count += 1
    if dif_count(S,N)+turn_count < result_count:
        result_count = dif_count(S,N)+turn_count
print(result_count)