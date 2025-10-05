a,b=map(int,input().split())

condition1=a % 3 != 0
condition2=a+1==b

if condition1 and condition2:
    print('Yes')
else:
    print('No')