N,L,R = map(int,input().split())
S = list(input())

check = ['o']*(R-L+1)

if S[L-1:R] == check:
    print('Yes')
else:
    print('No')