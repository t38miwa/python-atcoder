# 空ではない配列Aが与えられる
# 配列には奇数個の要素が含まれる
# ペアが作れない唯一の要素があるのでそれを返す
# 9 3 9 3 9 7 9
from collections import Counter

A = list(map(int,input().split()))

def solution(A):
    counter = Counter(A)
    d = dict(counter)
    for k,v in d.items():
        if v % 2 == 1:
            return k

print(solution(A))