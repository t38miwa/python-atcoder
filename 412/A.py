N = int(input())
count = 0
for i in range(N):
    A,B = map(int,input().split())
    if A < B:
        count += 1
print(count)