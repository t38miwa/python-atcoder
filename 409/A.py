N = int(input())
T = input()
S = input()

for i in range(N):
    if T[i] == 'o' and S[i] == 'o':
        print('Yes')
        exit()
print('No')