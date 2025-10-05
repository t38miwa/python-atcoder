X,Y=map(int,input().split())

if Y-X>2 and Y-X>=1:
    print('No')
elif Y-X<=2 and Y-X>=1:
    print('Yes')
elif Y-X >= -3 and Y-X <= -1:
    print('Yes')
elif Y-X < -3 and Y-X <= -1:
    print('No')