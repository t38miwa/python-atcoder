import sys
sys.setrecursionlimit(10**9)

N=int(input())
G=[[] for _ in range(N+1)]

# --- グラフ構築 ---
for i in range(1,N+1):
    a,b=map(int,input().split())
    G[a].append(i)
    G[b].append(i)
    print(f"スキル{i}は条件({a}, {b}) -> {a}->{i}, {b}->{i}")
print(G)

ok=[0]*(N+1)
ok[0]=1
print("初期状態: ok =", ok)

def dfs(v):
    print(f"dfs({v}) を開始")
    ok[v]=1
    for vv in G[v]:
        print(f" {v} から {vv} へ進める")
        if not ok[vv]:
            print(f"  {vv} は未訪問なので dfs({vv}) へ")
            dfs(vv)
        else:
            print(f"  {vv} はすでに訪問済み")

print("==== DFS 開始 ====")
dfs(0)
print("==== DFS 終了 ====")

print("訪問状態:", ok)
print("到達できたスキル数 =", sum(ok)-1)
