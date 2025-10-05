N = int(input())
S = input()

flag = True
if N % 2 != 1:
    flag = False

point = int(((N+1)//2))

if S[point-1] != '/':
    flag = False

for i in range(point-1):
    if S[i] != '1':
        flag = False
for j in range(point,N):
    if S[j] != '2':
        flag = False

if flag:
    print('Yes') 
else:
    print('No')   