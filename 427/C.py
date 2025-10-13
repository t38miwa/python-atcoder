# 無向グラフとは　グラフにおいて辺に方向がないグラフのこと

# 1.グラフが二部グラフであるか判定する
# 2.二部グラフでないなら適切な辺を削除する
# 3.二部グラフであれば答えを出力する

def is_graf():
    flag = False

    return flag


N,M = map(int,input().split())

G = {}

for i in range(N):
    G[i] = set()

print(G)

for i in range(M):
    u,v = map(int,input().split())
    G[u - 1].add(v - 1)
    G[v - 1].add(u - 1)

# 二部グラフでない限りループする
while flag == false:
    ans = is_graf()
    if ans:
    else:
    
