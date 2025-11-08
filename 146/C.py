# 9を買うには10*9+7*1 = 97円必要
# 所持金が100円の時、買える最大の整数は？

# 1から10**9までで二分探索を繰り返す

A,B,X = map(int,input().split())

def price(N):
    return A * N + B * len(str(N))

# 二分探索の関数
def binary_search(X):
    left = 0
    right = 1000000001
    while left +1 != right:
        mid = (left + right) // 2 
        if price(mid) <= X:
            left = mid
        else:
            right = mid
    return left

ans = binary_search(X)
print(ans)