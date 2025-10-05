AB,AC,BC = input().split()

if AB == '<':
    if AC == '<':
        if BC == '<':
            print('B')
        else:
            print('C')
    else:
        if BC == '>':
            print('A')
else:
    if AC == '<':
        if BC == '<':
            print('A')
    if AC == '>':
        if BC == '<':
            print('C')
        else:
            print('B')