N, M = map(int, input().split())

edges = [tuple(map(int, input().split())) for _ in range(M)]

# 削除するべき辺の数、つまり答え
ans = M

# 2^N 通りの塗り方を全部探索する
# 例：5個の頂点を白黒で塗り分ける方法は32通り
# 0〜31の値を５ビットの２進数で表現すると白黒での塗り分けを表現できる
# 00001なら一番右の1が頂点1の色、一番左の0が頂点5の色である
for bit in range(2 ** N):
    # ある塗り方をした時に、削除するべき辺の数
    delete_count = 0
    print(bit)
    for u ,v in edges:
        # ビットを頂点番号分右にシフトし、その最下位ビットが0か1かを判定
        # 両方が0,または1ならTrue、そうでないならFalse
        if (1 & (bit >> u)) == (1 & (bit >> v)):
            delete_count += 1
    # 今回の塗り方で削除した辺の数の合計が、今までの塗り方の最小値ならansに登録
    ans = min(ans,delete_count)
print(ans)