# T = tak??a?h?
# S =     nashi
T = input()
S = input()

might = []
for i in range(len(T)-len(S)+1):
    might.append(T[i:len(S)+i])


for i in range(len(might)):
    flag = True
    for j in range(len(S)):
        if might[i][j] == S[j] and might[i][j] != '?':
            flag = True
        elif might[i][j] != S[j] and might[i][j] != '?':
            flag = False
            break
    if flag:
        print('Yes')
        exit()

print('No')