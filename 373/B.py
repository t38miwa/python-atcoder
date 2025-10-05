s = input()
x = [0] * 26
for i in range(26):
    x[ord(s[i]) - ord("A")] = i

ans = 0
for i in range(25):
    ans += abs(x[i] - x[i + 1])
print(ans)