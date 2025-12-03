# 道は東西南北に1kmごとに並んでいる
# track中央交差点から東に2km進んだところにある南北に伸びる道を東2通りという
# 太郎くん3回命令する、2番目の命令はMoveです
# Moveは4,2が与えられ、4km東、2km北に移動する
# query east 東9通りを何回通ったか
# query north 北1通りを何回通ったか

import sys

def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    query = []
    for i, v in enumerate(lines):
        if i == 0:
            N = int(v)
        # print("line[{0}]: {1}".format(i, v))
        else:
            q = v.split()
            query.append(q)

    east_cnt = {}
    north_cnt = {}
    prev_east = 0
    prev_north = 0
    for i in range(N):
        if query[i][0] == 'MOVE':
            east = int(query[i][1])
            north = int(query[i][2])
            cnt_move(prev_east,prev_north,east,north,east_cnt,north_cnt)
            prev_east = east
            prev_north = north

        elif query[i][0] == "QUERY_EAST":
            # print(east_cnt)
            # print(pass_cnt)
            pass_cnt = int(query[i][1])
            if pass_cnt not in east_cnt:
                print(0)
            else:
                print(east_cnt[pass_cnt])

        elif query[i][0] == "QUERY_NORTH":
            # print(north_cnt)
            # print(pass_cnt)
            pass_cnt = int(query[i][1])
            if pass_cnt not in north_cnt:
                print(0)
            else:
                print(north_cnt[pass_cnt])
                
# qeuryがMOVEだった時に、移動した通りを辞書配列に記録する関数
def cnt_move(prev_east,prev_north,east,north,east_cnt,north_cnt):
        for j in range(prev_east,east+1):
            if j in east_cnt:
                east_cnt[j] += 1
            else:
                east_cnt[j] = 1

        for k in range(prev_north,north+1):
            if k in north_cnt:
                north_cnt[k] += 1
            else:
                north_cnt[k] = 1    

# 入力用
if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)