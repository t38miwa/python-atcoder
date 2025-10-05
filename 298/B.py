n=int(input())

a=[[0 for i in range(n)] for j in range(n)]
for i in range(n):  
    a[i]=list(map(int,input().split()))

b=[[0 for i in range(n)] for j in range(n)]
for i in range(n):  
    b[i]=list(map(int,input().split()))


def round():
    match=True
    for i in range(n):
        for j in range(n):
            if b[i][j]==1 and a[i][j]!=1:
                match=False
                break
    