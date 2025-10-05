"""AtCoder Beginner Contest 285 B"""
n = int(input())
s = list(input())
for i in range(1, n):
    result = n - i
    for j in range(n - i):
        if s[j] == s[i + j]:
            result = j
            break
    print(result)