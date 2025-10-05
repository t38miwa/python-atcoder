M,D = map(int,input().split())
y,m,d=map(int,input().split())

if d+1 > D and m+1 > M:
    y+=1
    m=1
    d=0
if d+1 > D and m+1 <= M:
    m+=1
    d=0

print(y,m,d+1)