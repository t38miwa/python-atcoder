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

# 条件1
Ym = Y * min(A)
XM = X * max(A)

# 条件2,3
P = 0
D = Y - X
for i in range(XM,Ym+1):
    r_lst = []
    for j in range(N):
        r = (i - X * A[j]) % D
        r_lst.append(r)
    # r_lst内の値が全て等しい = r,余りが全て等しい
    if len(set(r_lst)) != 1:
        print(-1)
        exit()
    if i > P:
        P = i

# 最終結果を求める
ans = 0
for i in range(N):
    yi = (P - X * A[i]) // D
    ans += yi
print(ans)