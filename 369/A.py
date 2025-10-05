a,b=map(int,input().split())

result=0
if a==b:
    result=1
elif abs(a-b)%2!=0:
    result=2
else:
    result=3

print(result)