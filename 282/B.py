n,m=map(int,input().split())
s = [input() for i in range(n)]

result=0
for i in range(n):
    for j in range(i+1,n):
        temp_f=True
        for k in range(m):
            if s[i][k]=='x' and s[j][k]=='x':
                temp_f=False
        if temp_f:
            result+=1

print(result)