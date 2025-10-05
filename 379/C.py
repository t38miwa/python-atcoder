N,K = map(int,input().split())
S = list(input())

T = ['O'] * K
W = ['X'] * K

count = 0
for i in range(N):
    if S[i:i+K] == T:
        count += 1
        S[i:i+K] = W

print(count)