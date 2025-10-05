# OSのバージョンはN個ある
# PCもN台、２番目のPCのOSバージョンは２
# おそらく普通に実装するとTLEになる
# まずはTLEになってもいいから実装をする

# 普通の実装完了した
# O(Q)×O(N) = 10^11でTLE
# ①バージョンが2以下のPCを探す
# ②バージョンが2以下ならカウントに追加
# ③2以下のPCを6にアップグレード
# minという変数を作り、そこに3を入れる

N,Q = map(int,input().split())

# PCのバージョンの初期状態
# PC = {}
# for i in range(N):
#     PC[i+1] = 1

PC = [1 for i in range(N)]

min = 0
for i in range(Q):
    X,Y = map(int,input().split())
    # 2 6の場合、バージョン2以下のPCをバージョン6にする

    # PCのキーがminからXの値の合計を出力する
    # 累積和で実装すればいけるのだろうか？
    sum = 0
    for j in range(min,X):
        sum += PC[j]
        PC[j] = 0
    if sum > 0:
        min = X

    # sum = sum(map(PC.get, range(min,X+1)))
    print(sum)
    PC[Y-1] += sum