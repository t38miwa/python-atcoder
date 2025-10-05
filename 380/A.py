N = input()

one = 0
two = 0
three = 0
for i in range(len(N)):
    if N[i] == '1':
       one += 1
    if N[i] == '2':
       two += 1
    if N[i] == '3':
       three += 1

if one == 1 and two == 2 and three == 3:
    print('Yes')
else:
    print('No')