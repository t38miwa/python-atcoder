n=int(input())

two=str(bin(n)[2:])
count=0

if two[-1:]=='1':
    print(0)
else:
    for i in range(1,len(two)):
        if two[-i]=='1':
            break
        if two[-i]=='0':
            count+=1
    print(count)