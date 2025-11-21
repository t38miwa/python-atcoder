#  条件1 78 <= P <= 80
#  条件2 Pを2で割った余り = 6Aiを2で割った余り = r
#       (80-6*11)/2 = 7 余り 0
#       (80-6*10)/2 = 10 余り 0
#       (80-6*13)/2 = 1 余り 0
#  条件3 Pが大きくなるほどyiも大きくなる
#       つまりP = 78のときより、P = 80のときの方がyiは大きくなる

# 解法 
# 条件2を満たさない場合は-1を出力
# 2で割った余りがrである80以下の最大の整数をPとする
# ただし、Pが78未満となるならば条件を満たすPは存在しないため、-1を出力する

N,X,Y = map(int,input().split())
A = list(map(int,input().split()))

def floor(a, b):
    return a // b

m = min(A)
M = max(A)

D = Y - X

# 条件2: 合同条件
r = (X * A[0]) % D
for Ai in A:
    if (X * Ai) % D != r:
        print(-1)
        exit()

P_max = Y * m

P_min = X * M

# 条件3: P_max 以下で P ≡ r (mod D) の最大の P
P = D * floor(P_max - r, D) + r

if P < P_min:
    print(-1)
    exit()

ans = 0
for Ai in A:
    yi = (P - X * Ai) // D
    ans += yi

print(ans)