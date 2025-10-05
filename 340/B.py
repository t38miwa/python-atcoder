q=int(input())
A=[]
for i in range(q):
    n,num=map(int,input().split())
    if n == 1:
        A.append(num)
    if n == 2:
        print(A[-num])