N=int(input())

A=list(map(int,input().split()))

sum=0

for i in range(N-1):
    sum+=A[i]

if sum>0:
    print(-(sum))
elif sum<0:
    print(-(sum))
else:
    print(0)