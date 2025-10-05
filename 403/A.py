N = int(input())
A = list(map(int,input().split()))

count = 0
for i in range(0,N,2):
    count += A[i]

print(count)