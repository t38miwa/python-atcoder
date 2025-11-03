# 5人の人が東西方向に一列に並んでいる
# 西から3番目をリーダーに任命
# リーダーの位置より西側にいる人に東を向いている数が多く、
# リーダーの位置より東側にいる人に西を向いている数が多い時に向く方向を変える人が少なくなる
N = int(input())
S = input()

cnt_w = [0] * (N+1)
cnt_e = [0] * (N+1)

for i in range(N):
    cnt_w[i+1] = cnt_w[i] + (1 if S[i] == 'W' else 0)
    cnt_e[i+1] = cnt_e[i] + (1 if S[i] == 'E' else 0)

min_change = N
for i in range(N+1):
    leader = i
    # リーダーから左側の西、東を向いている数
    if leader-1 >= 0:
        left_e = cnt_e[leader-1]
        left_w = cnt_w[leader-1]
    else:
        left_e = 0 
        left_w = 0
    right_e = cnt_e[N] - cnt_e[leader]
    right_w = cnt_w[N] - cnt_w[leader]
    # print(left_e,left_w,right_e,right_w)
    # leaderから西側の西側を向いている数と、leaderから東側の東側を向いてる数の総和が最も少ないとき、
    # 最小の回数で向く方向を変えられる
    if left_w + right_e <= min_change:
        min_change = left_w + right_e
print(min_change)