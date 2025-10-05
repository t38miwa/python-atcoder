A,B,C,D = map(int,input().split())

if A > C:
    print('Yes')
    exit()
elif A < C:
    print('No')
    exit()
else:
    if B > D:
        print('Yes')
        exit()
    else:
        print('No')