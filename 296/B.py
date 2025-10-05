s=[input() for i in range(8)]

for i in range(8):
    for j in range(8):
        if s[i][j]=='*':
            resultx=chr(ord('a')+j)
            resulty=8-i
print(resultx,resulty,sep='')