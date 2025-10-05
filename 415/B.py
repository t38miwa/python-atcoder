S = list(input())

# 荷物の総数mを求める
m = 0
for i in range(len(S)):
    if S[i] == '#':
        m += 1


for i in range(m//2):
    result = []
    for j in range(len(S)):
        if S[j] == '#':
            result.append(j+1)
            S[j] = '.'
        if len(result) == 2:
            print(str(result[0])+','+str(result[1]))
            break