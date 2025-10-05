N = int(input())
L = list(map(int,input().split()))

x = 0
y = 0
for i in range(N):
    if L[i] == 1:
        x = i
        break

for i in range(N-1,-1,-1):
    if L[i] == 1:
        y = i
        break

print(y-x)