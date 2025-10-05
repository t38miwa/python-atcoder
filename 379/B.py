N,K = map(int,input().split())
S = list(input())

count = 0
# for i in range(N-2):
#     if S[i] == 'O' and S[i+1] == 'O' and S[i+2] == 'O':
#         count += 1
#         S[i] = 'X'
#         S[i+1] = 'X'
#         S[i+2] = 'X'

k_count = 0
for i in range(N):
    for j in range(K-i):
        if S[i+j] == 'O':
            k_count += 1
    if k_count == K:
        count += 1
        

print(count)