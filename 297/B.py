s = list(input())

bf_index = 1
bs_index = 1
k_index = 1
rf_index = 1
rs_index = 1
result1 = False
result2 = False

for i in range(len(s)):
    if bf_index == 1 and s[i] == 'B':
        bf_index = i  # 最初に見つけたBの位置
    elif bf_index != 1 and s[i] == 'B':
        bs_index = i  # 2つ目に見つけたBの位置

    if s[i] == 'K':
        k_index = i  # Kの位置

    if rf_index == 1 and s[i] == 'R':
        rf_index = i  # 最初に見つけたRの位置
    elif rf_index != 1 and s[i] == 'R':
        rs_index = i  # 2つ目に見つけたRの位置

# 条件1: Bの偶奇が異なるか
if (bf_index % 2 != bs_index % 2):
    result1 = True

# 条件2: Kが2つのRの間にあるか
if rf_index < k_index < rs_index:
    result2 = True

# 最終判定
if result1 and result2:
    print("Yes")
else:
    print("No")
