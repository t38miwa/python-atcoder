# 4分以上運転するなら2分以上休憩を取る必要がある
# 長さ11の文字列
# 1<= l <= r <= 11
# Sのlからr文字目までに含まれるaの個数が4以上
# Sのlからr文字目までに含まれるbの個数がB未満

N,A,B = map(int,input().split())
S = list(input())

for i in range(N):
    for j in range(N):
        sum_A = S[i:j].count('a')
        sum_B = S[i:j].count('b')
        if sum_A >= A and sum_B < B:
            print(i+1,j,S[i:j])