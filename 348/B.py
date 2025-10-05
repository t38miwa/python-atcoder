import math

n=int(input())

x=[]
y=[]
for i in range(n):
    xi,yi=map(int,input().split())
    x.append(xi)
    y.append(yi)


for i in range(n):
    result_index=0
    far=0
    for j in range(n):
        ans=math.sqrt((x[i]-x[j])**2+(y[i]-y[j])**2)
        if ans>far:
            far=ans
            result_index=j
    print(result_index+1)