x = sorted(input())
print(x)
for i in range(len(x)):
    if x[i] > '0':
        x[0], x[i] = x[i], x[0]
        break
print(''.join(x))