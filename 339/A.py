S=list(input())
index=[]

for i in range(len(S)):
    if S[i]=='.':
        index.append(i)

last_index=index[-1]
print(''.join(S[last_index+1:]))