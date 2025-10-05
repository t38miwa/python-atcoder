n=int(input())

for i in range(n,920):
    hundred=i//100
    ten=(i%100)//10
    one=i%10
    if hundred*ten==one:
        print(i)
        break