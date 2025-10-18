# N個の皿、M個の条件
# 条件は皿A,Bにボールが１個以上あるとき満たされる
# K人の人がいる
# 人iは皿C,Dどちらかにボールをおく
# 満たされる条件の個数は？

N,M = map(int,input().split())
A = []
B = []
for i in range(M):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)

K = int(input())

C = []
D = []
for i in range(K):
    c,d = map(int,input().split())
    C.append(c)
    D.append(d)

def match(result):
    count = 0
    for i in range(M):
        if A[i] in result and B[i] in result:
            count += 1
    return count

# 組み合わせを表現する
ans = 0
for bit in range(1 << K):
    subset = []
    result = []
    for i in range(K):
        if bit >> i & 1:
            subset.append(i)
            result.append(D[i])
        else:
            result.append(C[i])
    count = match(result)
    if count > ans:
        ans = count
print(ans)