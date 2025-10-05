N = int(input())
D = [int(input()) for _ in range(N)]
# まずソートする
sorted_d = sorted(D,reverse=True)

count = 0
result = []
for i in range(N):
    # 存在しないならリストに追加する
    if sorted_d[i] not in result:
        result.append(sorted_d[i])

print(len(result))