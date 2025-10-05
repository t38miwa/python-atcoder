n,m=map(int,input().split())
s=input()
t=input()

if s==t[:n] and s==t[m-n:]:
    print(0)
elif s==t[:n] and s!=t[m-n:]:
    print(1)
elif s!=t[:n] and s==t[m-n:]:
    print(2)
elif s!=t[:n] and s!=t[m-n:]:
    print(3)