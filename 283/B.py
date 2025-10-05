n=int(input())
a=list(map(int,input().split()))
q=int(input())
query=[list(map(int,input().split())) for i in range(q)]

for i in range(q):
    if query[i][0]==2:
        index=query[i][1]-1
        print(a[index])
    elif query[i][0]==1:
        index=query[i][1]-1
        a[index]=query[i][2]
