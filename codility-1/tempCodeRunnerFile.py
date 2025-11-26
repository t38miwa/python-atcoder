# カエルは最初位置0
# 位置X+1に行きたい
# 時刻2に位置1に葉が落ちる
# カエルが川を渡れる最も早い時刻は？
# 全ての位置に葉があるときのみ川を渡れる

def solution(A,X):
    seen = set()
    for i in range(len(A)):
        if A[i] not in seen:
            seen.add(A[i])
        if len(seen) == X:
            return i
    return -1

A = list(map(int,input().split()))
X = int(input())

print(solution(A,X))