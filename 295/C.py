# 6枚の靴下、２枚めの靴下の色は1
# 同じ色の靴下を２枚選んでペアにする
from collections import Counter

N = int(input())
A = list(map(int,input().split()))

counter = Counter(A)
d = dict(counter)

ans = 0
for k,v in d.items():
    ans += v // 2
print(ans)