n,q=map(int,input().split())
t=list(map(int,input().split()))

teeth=[1]*n

for i in range(q):
    index=t[i]-1
    if teeth[index] == 1:
        teeth[index]=0
    else:
        teeth[index]=1

count=0
for i in range(n):
    if teeth[i]==1:
        count+=1

print(count)