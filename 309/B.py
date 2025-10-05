"""AtCoder Beginner Contest 309 B"""
n = int(input())
a = [input() for i in range(n)]
b = ["" for i in range(n)]

b[0] += a[1][0]
for j in range(n - 1):
    b[0] += a[0][j]
for i in range(1, n - 1):
    b[i] += a[i + 1][0]
    for j in range(1, n - 1):
        b[i] += a[i][j]
    b[i] += a[i - 1][n - 1]
for j in range(n - 1):
    b[n - 1] += a[n - 1][j + 1]
b[n - 1] += a[n - 2][n - 1]

for i in range(n):
    print(b[i])