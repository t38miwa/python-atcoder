N,D = map(int,input().split())
# 1からDまでの整数Kでヘビの長さがK伸びた時、すべてのヘビの中から最も重いヘビの重さを出力する
# ヘビの重さ = T * (L+K)
T = []
L = []
for i in range(N):
        t,l = map(int,input().split())
        T.append(t)
        L.append(l)

# 1からDまで長さが伸びた時の重さを出力する
for k in range(1,D+1):
    most_heavy = 0
    # それぞれのヘビの重さを計算して、最も重いヘビをmost heavyとして出力する
    for i in range(N):
        result = T[i] * (L[i]+k)
        if most_heavy < result:
            most_heavy = result
    print(most_heavy)