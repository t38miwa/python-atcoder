"""AtCoder Beginner Contest 364 A"""
n = int(input())
s = [input() for i in range(n)]

result = True
for i in range(n - 2):
    if s[i] == "sweet" and s[i + 1] == "sweet":
        result = False
        break

print("Yes" if result else "No")