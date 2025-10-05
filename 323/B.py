"""AtCoder Beginner Contest 323 B"""
n = int(input())
s = [input() for i in range(n)]

a = []
for i in range(n):
    win = 0
    for j in range(n):
        if s[i][j] == 'o':
            win += 1
    a.append((-win, i + 1))
a.sort()

print(*[i for _, i in a])