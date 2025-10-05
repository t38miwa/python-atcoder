N=int(input())

S=list(map(int,input().split()))

result=[]
result.append(str(S[0]))
for i in range(N-1):
    sum=S[i+1]-S[i]
    result.append(str(sum))

print(' '.join(result))