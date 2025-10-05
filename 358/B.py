n,a=map(int,input().split())

t=list(map(int,input().split()))

wait=0
for i in range(n):
    if t[i] < wait:
        ans=a+wait
        print(ans)
        wait=ans
    else:
        ans=t[i]+a
        print(ans)
        wait=ans