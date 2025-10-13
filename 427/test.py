import sys

sys.setrecursionlimit(400000)

N, M = map(int, input().split())

G = {}  # 隣接リストを表す辞書
for i in range(N):
    G[i] = set()  # 頂点iに隣接する頂点の集合

for i in range(M):
    A, B = map(int, input().split())

    # 無向グラフなので、両方向に辺を張る
    G[A - 1].add(B - 1)
    G[B - 1].add(A - 1)

# 訪問済み頂点を記録する配列を用意する
group = [-1] * N
group[0] = 0

def dfs(G, v):
    for s in G[v]:
        if group[s] != -1:
            if group[s] == group[v]:
                return False
            continue

        group[s] = 1 if group[v] == 0 else 0
        if not dfs(G, s):
            return False
    return True

# グラフが連結でない可能性があるので全ての要素に対してdfsを行う
ok = dfs(G, 0)
for v in range(1, N):
    if group[v] != -1:
        continue
    if not dfs(G, v):
        ok = False
        break

print(G)
print("Yes" if ok else "No")

# １回目は普通に回す