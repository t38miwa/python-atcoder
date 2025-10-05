# 7の0から3乗までの合計が答え
N,M = map(int,input().split())

result = 0
for i in range(M+1):
    result += N**i

if result <= 10**9:
    print(result)
else:
    print('inf')