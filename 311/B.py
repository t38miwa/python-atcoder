"""AtCoder Beginner Contest 311 B"""
n, d = map(int, input().split())
s = [input() for i in range(n)]

result_str = ""
for i in range(d):
    this_time = True
    for j in range(n):
        if s[j][i] != 'o':
            this_time = False
    result_str += 'o' if this_time else 'x'

result = 0
now = 0
for i in range(d):
    if result_str[i] == 'o':
        now += 1
        result = max(result, now)
    else:
        now = 0

print(result)