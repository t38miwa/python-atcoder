# 電球1は2個のスイッチに繋がっている
#スイッチ1,2のうちonになっているスイッチの個数を割った余り0に等しい時に点灯
def bitsum(k,s,p):
    for bit in range(1<<N):
        subset = []
        for i in range(N):
            # bit = 01 10
            if bit & (1 << i):
                subset.append(i+1)
        if subset == s and len(subset) % 2 == p:
            print("subset",subset)
        if subset == s and len(subset) % 2 != p:
            print("subset",subset,"No")

N,M = map(int,input().split())
k = []
s = []
for i in range(M):
    data = list(map(int,input().split()))
    k.append(data[0])
    s.append(data[1:])
P = list(map(int,input().split()))

for i in range(M):
    bitsum(k[i],s[i],P[i])
# off off 00
# off on  01
# on  off 10
# on  on  11