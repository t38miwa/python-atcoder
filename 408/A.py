N,S = map(int,input().split())
T = list(map(int,input().split()))

last_hit = 0
sleep = S+0.5
for i in range(N):
    if T[i] - last_hit >= sleep:
        print('No')
        exit()
    else:
        last_hit = T[i]
print('Yes')