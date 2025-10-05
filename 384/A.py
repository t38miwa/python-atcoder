N,C1,C2 = input().split()
N = int(N)
S = list(input())

for i in range(N):
    if S[i] != C1:
        S[i] = C2

print(''.join(S))