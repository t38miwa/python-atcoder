H,W,X,Y = map(int,input().split())
S = [list(input()) for _ in range(H)]
T = input()

X -= 1
Y -= 1
count = 0
index = []
for i in range(len(T)):
    if T[i]=='U' and S[X-1][Y]!='#': X-=1
    if T[i]=='D' and S[X+1][Y]!='#': X+=1
    if T[i]=='L' and S[X][Y-1]!='#': Y-=1
    if T[i]=='R' and S[X][Y+1]!='#': Y+=1
    if S[X][Y] == '@':
        count += 1
        S[X][Y] = '.'

print(X+1,Y+1,count)