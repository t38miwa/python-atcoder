N,K = map(int,input().split())
A = list(map(int,input().split()))

# ①1にA1をかけた値を表示、この操作をN会繰り返す
result = 1
for i in range(N):
    result *= A[i]
    # もしK桁より上の桁数ならresultを1にする
    if len(str(result)) > K:
        result = 1
print(result)