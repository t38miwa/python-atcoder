"""AtCoder Beginner Contest 303 B"""
n, m = map(int, input().split())
a = [[0 for i in range(n)] for j in range(m)]
for i in range(m):
    a[i] = list(map(int, input().split()))

p = set()
for i in range(m):
    for j in range(n - 1):
        if a[i][j] <= a[i][j + 1]:
            p.add((a[i][j], a[i][j + 1]))
        else:
            p.add((a[i][j + 1], a[i][j]))

print(n * (n - 1) // 2 - len(p))