n,q=map(int,input().split())
player=[0] * (n+1)

for i in range(q):
    e,x=map(int,input().split())
    if e==3:
        if player[x]>=2:
            print('Yes')
        else:
            print('No')
    if e==2:
        player[x]+=2
    if e==1:
        player[x]+=1
