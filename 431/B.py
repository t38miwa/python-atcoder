# はじめロボットの重さは31
# 同時に取り付けられる部品が4つある
# 種類3の重さは65
# 4個のクエリを処理せよ
# ロボットに種類3の部品がついていない場合は取り付け、ついている場合は取り外す。
# その後にロボットの重さを出力する

X = int(input())
N = int(input())
W = list(map(int,input().split()))
Q = int(input())

have = []
ans = X
for i in range(Q):
    P = int(input())
    if P in have:
        have.remove(P)
        ans -= W[P-1]
        print(ans)
    else:
        have.append(P)
        ans += W[P-1]
        print(ans)