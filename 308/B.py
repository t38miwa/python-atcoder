n,m=map(int,input().split())
c=list(input().split())
d=list(input().split())
p=list(map(int,input().split()))


price={}

for i in range(m):
    price[d[i]]=p[i+1]

result=0

for i in range(n):
    if not  c[i] in price:
        result+=p[0]
    else:
        result+=price[c[i]]

print(result)