n=int(input())
t=[[0 for j in range(100)] for i in range(100)]

for i in range(n):
    a,b,c,d=map(int,input().split())
    for x in range(a,b):
        for y in range(c,d):
            t[x][y]+=1

result=0

for i in range(100):
    for j in range(100):
        if t[i][j]>0:
            result+=1

print(result)