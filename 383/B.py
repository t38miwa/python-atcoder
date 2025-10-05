H,W,D = map(int,input().split())

# 番兵の用意
S = [input() for i in range(H)]

# マンハッタン距離を求める関数
def diff(p1,p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

humid_grid = []
for i in range(H):
    for j in range(W):
        if S[i][j] == '.':
            # 加湿器を配置できるマスを記録する
            humid_grid.append((i,j))

result = 0

# 例　(1,1)マス
for h1 in range(len(humid_grid)):
    # 例　(1,5)マス
    for h2 in range(h1+1,len(humid_grid)):
        t_result = 0
        # 例 (1,1),(2,1)など 
        for f3 in humid_grid:
            # どちらからかの距離がD以下なら値を追加
            if diff(f3,humid_grid[h1]) <= D or diff(f3,humid_grid[h2]) <= D:
                t_result += 1
        result = max(result, t_result)
        
print(result)