from collections import Counter
import math

N = int(input())
A = list(map(int, input().split()))

# 各値の出現回数をカウント
count = Counter(A)

ans = 0
for k,v in count.items():
    if v >= 1:
        pairs = math.comb(v, 2)
        others = N - v
        ans += pairs * others

print(ans)