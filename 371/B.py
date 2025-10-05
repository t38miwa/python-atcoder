N,M = map(int,input().split())

# その特定の家の初めてのMの場合はYesを出力
result = [1]*N
for i in range(M):
    A, B = input().split()
    A = int(A)
    if result[A-1] == 1 and B == 'M':
        print('Yes')
        result[A-1] = 0
    else:
        print('No')