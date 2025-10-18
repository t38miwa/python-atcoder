m = int(input())

result = []
for i in range(11):
    t = m % 3
    m //= 3
    for j in range(t):
        result.append(i)
print(len(result))
print(*result)