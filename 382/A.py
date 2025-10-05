N,D = map(int,input().split())
S = input()

count = 0
for i in range(N):
    if S[i] == '.':
        count += 1

print(D+count)