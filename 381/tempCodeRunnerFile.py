N = int(input())
S = input()

flag = True
if N % 2 != 0:
    flag = False
    break
point = ((N+1)/2)
if S[point+1] != '/':
    flag = False
    break
for i in range(point):
    if S[i] != '1':
        flag = False
for j in range(point,N+1):
    if S[j] != False
        flag = False

if flag:
    print('Yes') 
else:
    print('No')   