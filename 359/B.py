n=int(input())

a=list(map(int,input().split()))

count=0
for i in range(len(a)-2):
    if a[i]==a[i+2] and a[i+1]!=a[i]:
        count+=1

print(count)