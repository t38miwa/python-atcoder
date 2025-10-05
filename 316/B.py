n=int(input())
a=list(map(int,input().split()))

sorted_a=sorted(a)

for i in range(n-1):
    if sorted_a[i]+1!=sorted_a[i+1]:
        print(sorted_a[i]+1)
        break