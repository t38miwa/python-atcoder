n, t = map(int, input().split())
c = list(map(int, input().split()))
r = list(map(int, input().split()))

# 初期化
target_scores = []
default_scores = []
target_index = -1
default_index = -1

# 比較対象となる値をリストに追加
for i in range(n):
    if c[i] == t:
        target_scores.append(r[i])
        if target_index == -1 or r[i] > r[target_index]:
            target_index = i
    elif c[i] == c[0]:
        default_scores.append(r[i])
        if default_index == -1 or r[i] > r[default_index]:
            default_index = i

# 結果の出力
if target_index != -1:
    print(target_index + 1)  # 配列インデックスは0からなので1を足す
else:
    print(default_index + 1)
