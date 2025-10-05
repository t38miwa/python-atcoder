n,m=map(int,input().split())

#目標摂取量
a=list(map(int,input().split()))
sum_x = [0] * m

result=True
for i in range(n):
    x=list(map(int,input().split()))
    for j in range(m):
        sum_x[j]+=x[j]
    print(sum_x)

for i in range(m):
    if sum_x[i]<a[i]:
        result=False

if result:
    print('Yes')
else:
    print('No')