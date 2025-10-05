n,l,r=map(int,input().split())
a=list(map(int,input().split()))

for i in range(n):
    num=a[i]
    result=[]
    for j in range(l,r+1):
        result.append(abs(j-num))
    print(result)