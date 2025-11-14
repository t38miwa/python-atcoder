#3人の生徒からなるクラス
# ２番目の生徒の身長は160cm
# 3人のうち身長が120cm以上の生徒は何人か

# Aのリストをソートする
# 120cm以下になるindexを二分探索で探す

N,Q = map(int,input().split())
A = list(map(int,input().split()))
x = [int(input()) for _ in range(Q)]

sort_A = sorted(A)

def binary_search(A,x):
    left = 0
    right = N
    while left < right:
        mid = (left + right) // 2
        if x > sort_A[mid]:
            left = mid + 1
        else:
            right = mid
    return left

for i in range(Q):
    index = binary_search(sort_A,x[i])
    print(N - index)