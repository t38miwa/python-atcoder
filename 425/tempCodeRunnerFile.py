import sys
input = sys.stdin.readline

n, q = map(int, input().split())
a = list(map(int, input().split()))
# 4回転すると元の配列にもどるため、２倍にすることで回転を開始位置のシフトとして表現することができる
b = a + a
print(b)
# 後ろから回すことでi移行の要素の合計を知れる
for i in range(2 * n - 1, 0, -1):
    print(b[i - 1],b[i])
    b[i - 1] += b[i]
print(b)
# [26, 23, 22, 18, 13, 10, 9, 5]
rui_c = 0
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        c = query[1]
        rui_c = c
        rui_c %= n
    else:
        l, r = query[1] - 1, query[2]
        # l = 1-1,r = 3
        # b[0] = 26,
        # b[3] = 18
        print(b[l + rui_c] - b[r + rui_c])
