# カエルが道路の向こう側に行こうとしている
# カエルは現在位置Xにいて、位置Y以上に到達したい
# カエルは常にDジャンプできる
# 10 85 30

X,Y,D = map(int,input().split())

def solution(X, Y, D):
    dis = Y - X
    i = 0
    ans = 0
    while ans < dis:
        i += 1
        ans = i * D
    return i

print(solution(X,Y,D))