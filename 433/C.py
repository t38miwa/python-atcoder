s = input()
n = len(s)
ans = 0
for i in range(n - 1):
    if int(s[i]) + 1 != int(s[i + 1]):
        continue
    j = i
    while j != -1 and s[j] == s[i]:
        j -= 1
    k = i + 1
    while k != n and s[k] == s[i + 1]:
        k += 1
    ans += min(i - j, k - i - 1)
print(ans)