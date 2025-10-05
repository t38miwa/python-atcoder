n,k=map(int,input().split())

a=list(map(int,input().split()))

ans_count=0
index=0
vacant=k

while index<n:
    if k<a[index]:
        ans_count+=1
        k=vacant
    else:
        k-=a[index] 
        index+=1
ans_count+=1

print(ans_count)