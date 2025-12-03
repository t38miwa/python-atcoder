# 道は東西南北に1kmごとに並んでいる
# track中央交差点から東に2km進んだところにある南北に伸びる道を東2通りという
# 太郎くん3回命令する、2番目の命令はMoveです
# Moveは4,2が与えられ、4km東、2km北に移動する
# query east 東9通りを何回通ったか
# query north 北1通りを何回通ったか

N = int(input())
query = [input().split() for _ in range(N)]

# qeuryがMOVEだった時に、移動した通りを辞書配列に記録する関数
def cnt_move(east, north, east_cnt, north_cnt):
    # 東方向の移動（南北に伸びる通りを通過）
    if east != 0:
        
        start = min(prev_east, east)
        end = max(prev_east, east)
        # print(start,end)
        for j in range(start + 1, end + 1):  # 端点を除く
            east_cnt[j] = east_cnt.get(j, 0) + 1
    
    # 北方向の移動（東西に伸びる道を通過）
    if north != 0:
        north += prev_north
        print(prev_north,north)
        start = min(prev_north, north)
        end = max(prev_north, north)
        # print(start,end)
        for k in range(start + 1, end + 1):  # 端点を除く
            north_cnt[k] = north_cnt.get(k, 0) + 1

east_cnt = {}
north_cnt = {}
for i in range(N):
    if query[i][0] == 'MOVE':
        east = int(query[i][1])
        north = int(query[i][2])
        cnt_move(east,north,east_cnt,north_cnt)
        prev_east = east
        prev_north = north

    elif query[i][0] == "QUERY_EAST":
        pass_cnt = int(query[i][1])
        # print(east_cnt)
        # print(pass_cnt)
        if pass_cnt not in east_cnt:
            print(0)
        else:
            print(east_cnt[pass_cnt])

    elif query[i][0] == "QUERY_NORTH":
        pass_cnt = int(query[i][1])
        # print(north_cnt)
        # print(pass_cnt)
        if pass_cnt not in north_cnt:
            print(0)
        else:
            print(north_cnt[pass_cnt])