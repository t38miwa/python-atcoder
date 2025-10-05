n=int(input())
a=list(map(int,input().split()))

max_a=max(a)

for i in range(n):
    if a[i]==max_a:
        a[i]=0

print(max(a))