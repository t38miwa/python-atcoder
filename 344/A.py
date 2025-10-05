S=list(input())

index=[]
for i in range(len(S)):
    if S[i]=='|':
        index.append(i)

start=index[0]
end=index[1]

print(''.join(S[:start])+''.join(S[end+1:]))