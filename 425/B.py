N = int(input())
A = list(map(int,input().split()))

# -1でない数字の部分はA[i] = P[i]にする
P = [0]*N
for i in range(N):
    if A[i] != -1:
        P[i] = A[i]

# リスト内に重複がある場合は即座にNoを出力
for i in range(1,N+1):
    count_P = P.count(i)
    if count_P > 1:
        print('No')
        exit()

# すでに存在する数字の部分はそのままで他のところに先頭から数字を追加
check = []
for i in range(1,N+1):
    if i not in P:
        check.append(i)

for i in range(N):
    if P[i] == 0 and len(check) >= 1:
        P[i] = check[0]
        check.pop(0)
print('Yes')
print(*P)