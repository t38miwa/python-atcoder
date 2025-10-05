n,c=map(int,input().split())

t=list(map(int,input().split()))

count = 1
index = 0
for i in range(n):
    if t[i] - t[index] >= c:
        count += 1
        index = i

print(count)