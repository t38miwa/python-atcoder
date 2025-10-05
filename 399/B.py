# N人がコンテストに出場、得点はP
N = int(input())
P = list(map(int,input().split()))

# dicを作る　{人1:3点,人2:12点,人3:9点,人4:9点}
dic = {}
for i in range(N):
    dic[i+1] = P[i]
# ソートする　
sorted_dic = dict(sorted(dic.items(), key=lambda x: x[1],reverse=True))
# {人2:12点,人3:9点,人4:9点,人1:3点}
# 順位をつける　rで順位管理、pointで最大得点を管理
prev_point = 0
r = 0
plus = 0
for key in sorted_dic:
    if sorted_dic[key] == prev_point:
        prev_point = sorted_dic[key]
        sorted_dic[key] = r
        plus += 1
    else:
        r += 1
        r += plus
        plus = 0
        prev_point = sorted_dic[key]
        sorted_dic[key] = r

# グリッドの90度右回転実装
# 4x4グリッドの例
grid = [
    ['#', '#', '#', '.'],
    ['.', '.', '.', '#'],
    ['.', '.', '.', '#'],
    ['.', '.', '.', '#']
]

# 90度右回転後のグリッドを作成
n = len(grid)
rotated_grid = [['' for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        # 90度右回転: (i, j) -> (j, n-1-i)
        rotated_grid[j][n-1-i] = grid[i][j]

# 回転後のグリッドを出力
print("90度右回転後:")
for row in rotated_grid:
    print(''.join(row))

# 人順にソート
p_dic = dict(sorted(sorted_dic.items(), key=lambda x: x[0]))
for v in p_dic.values():
    print(v)