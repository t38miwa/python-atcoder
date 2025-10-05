N = int(input())

A = list(map(int,input().split()))

result = True
for i in range(N-1):
    if A[i] >= A[i+1]:
        result = False
        break

print('Yes' if result else 'No')