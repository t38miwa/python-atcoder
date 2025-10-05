"""AtCoder Beginner Contest 294 B"""
h, w = map(int, input().split())
a = [[0 for i in range(w)] for j in range(h)]
for i in range(h):
    a[i] = list(map(int, input().split()))

for i in range(h):
    s = ""
    for j in range(w):
        if a[i][j] == 0:
            s += "."
        else:
            s += chr(a[i][j] + ord ('A') - 1)
    print(s)