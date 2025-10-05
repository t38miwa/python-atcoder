n=int(input())

result=False
for x in range(100):
    for y in range(100):
        if (2**x)*(3**y)==n:
            result=True
            break

if result:
    print('Yes')
else:
    print('No')