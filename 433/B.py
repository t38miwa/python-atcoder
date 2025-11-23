# 4人の人が並んでいる
# 左から2人目の人を人2と呼ぶ、この人の身長は3

# 計算量は考慮しなくてよさそう
# 自分より左にいる人のリストを毎度作成する
# リストに対してfor文を回し、リスト内の身長-自分の身長の値が0以上かつ最も小さいindexを求める

N = int(input())
A = list(map(int,input().split()))

for i in range(N):
    left_lst = A[:i]
    ## 一つ目は必ず-1
    if len(left_lst) == 0:
        print(-1)
        continue
    ans = 0
    for j in range(len(left_lst)):
        height_diff = left_lst[j] - A[i]
        if height_diff > 0:
            ans = j+1
    if ans == 0:
        print(-1)
    else:
        print(ans)
