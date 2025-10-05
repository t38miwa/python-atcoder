N,S,K=map(int,input().split())
pairs=[]

for i in range(N):
    P,Q=map(int,input().split())
    sum=P*Q
    pairs.append(sum)

result=0
for i in range(N):
    result+=pairs[i]

if result<S:
    print(result+K)
else:
    print(result)
