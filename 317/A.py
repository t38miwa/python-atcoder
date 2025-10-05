def find_min_potion_index(N, H, X, P):
    for i in range(N):
        if H + P[i] >= X:
            return i + 1  # インデックスは1から始まるので+1

# 入力を受け取る
N, H, X = map(int, input().split())
P = list(map(int, input().split()))

# 最も効き目の弱い傷薬の番号を出力
print(find_min_potion_index(N, H, X, P))
