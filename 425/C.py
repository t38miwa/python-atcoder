N,Q = map(int,input().split())
A = list(map(int,input().split()))

for i in range(Q):
    q = list(map(int,input().split()))

    # q[0]が1の場合はAの先頭の要素を末尾に移動させる操作をc回行う。
    if q[0] == 1:
        c = q[1]
        A = A[c:N]+A[0:c]
    if q[0] == 2:
        l = q[1]
        r = q[2]
        print(sum(A[l-1:r]))