n = int(input())
a = list(map(int, input().split()))

result = [a[0]]
for i in range(1, n):
    if abs(a[i] - a[i - 1]) == 1:
        result.append(a[i])
    else:
        if a[i] - a[i - 1] > 0:
            for j in range(a[i - 1] + 1, a[i] + 1):
                result.append(j)
        else:
            for j in range(a[i - 1] - 1, a[i] - 1, -1):
                result.append(j)

# リストをスペース区切りで出力
print(" ".join(map(str, result)))
