m=int(input())
d=list(map(int, input().split()))
sum=0

for i in range(m):
    sum+=d[i]

result=int((sum+1)//2)
print(result)

new_sum=0

result_index=0
date=0
for i in range(m):
    new_sum+=d[i]
    if new_sum>=result:
        result_index=i+1
        date=new_sum-d[i]
        break
print(result_index,result-date)