N,A,B=map(int,input().split())
C=list(map(int,input().split()))

result=A+B

for i in range(N):
    if C[i]==result:
        index=i
print(index+1)