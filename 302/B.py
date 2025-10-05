h,w=map(int,input().split())

s=[input() for i in range(h)]

result=[]
for i in range(h):
    if s[i][j]=='s':
        result.append(s[i][j])
        for j in range(w):
            result.append(s[i][j])
            if ''.join(result)=='sunuke':