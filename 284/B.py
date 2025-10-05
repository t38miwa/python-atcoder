t=int(input())

all_count=[]
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    count=0
    for j in range(n):
        if a[j]%2==1:
            count+=1
    all_count.append(count)

for i in range(t):
    print(all_count[i])