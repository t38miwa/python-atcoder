N,X,Y,Z=map(int,input().split())

if X-Y>0:
    for i in range(Y,X):
        if i == Z:
            print('Yes')
            break
    else:
        print('No')
        
if X-Y<0:
    for i in range(X,Y):
        if i == Z:
            print('Yes')
            break
    else:
        print('No')

