n= int(input())
d=list(map(int,input().split()))

count=0
for i in range(1,n):
    day=d[i]
    for j in range(1,day):
        ten=j//10
        one=j%10
        if i==j:
            count+=1
            print(i,j)
        if i==ten and i==one:
            count+=1
            print(i,j)
        
print(count)