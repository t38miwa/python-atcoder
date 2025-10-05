N=int(input())

H=list(map(int,input().split()))

result=[]
for i in range(N):
    if H[i]>H[0]:
        result.append(i)

if result:
    print(result[0]+1)
else:
    print(-1)