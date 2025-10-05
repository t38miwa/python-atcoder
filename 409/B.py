N = int(input())
A = list(map(int,input().split()))

for i in range(N+1):
    count = 0
    for j in range(N):
        if A[j] >= i:
            count += 1   
    if count < i:
        print(i-1)
        exit()

# すべてのiで条件を満たした場合
print(N)