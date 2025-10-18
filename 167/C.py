# M個のアルゴリズムを学びたい
# N札の参考書でそれぞれCi円
# A1,2なら２番目のアルゴリズムの理解度が7上がる
# 全てのアルゴリズムの理解度をX以上にしたい

C = []
A = []
N,M,X = map(int,input().split())
for i in range(N):
    data = list(map(int,input().split()))
    C.append(data[0])
    A.append(data[1:])


# 目標達成可能か調べる
for i in range(M):
    sum_und = 0
    # ３冊
    for j in range(N):
        sum_und += A[j][i]
    if sum_und < X:
        print(-1)
        exit()

ans = sum(C)
for bit in range(1 << N):
    subset = []
    list_i = []
    for i in range(N):
        if bit >> i & 1:
            subset.append(C[i])
            list_i.append(i)
    und = sum(subset)
    # 全てのアルゴリズムの理解度が10以上になるか
    flag = True
    for i in range(M):
        sum_A = 0
        for j in range(len(list_i)):
            index = list_i[j]
            sum_A += A[index][i]
        if sum_A < X:
            flag = False
    # 今回の集合の合計が最小値、かつ理解度が全て10以上
    if und < ans and flag == True:
        ans = und

print(ans)