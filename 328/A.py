N,X=map(int,input().split())
S=list(map(int,input().split()))

result=0
for i in range(N):
    if S[i]<= X:
        result+=S[i]

print(result)