A,B,C = map(int,input().split())

lt = []

lt.append(A)
lt.append(B)
lt.append(C)

lt.sort(reverse=True)
new_lt = list(map(str,lt))

print(''.join(new_lt))