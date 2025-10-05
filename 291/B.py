n=int(input())

x=list(map(int,input().split()))

for i in range(n):
    x.remove(max(x))
    x.remove(min(x))

print(sum(x)/len(x))