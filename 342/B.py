n=int(input())
p=list(map(int,input().split()))

q=int(input())



for i in range(q):
    a,b=map(int,input().split())
    for j in range(n):
        if p[j]==a:
            print(a)
            break
        if p[j]==b:
            print(b)
            break