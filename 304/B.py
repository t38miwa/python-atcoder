n=int(input())

if n <= (10 ** 3)-1:
    print(n)
else:   
    for i in range(3,9):
        if n >= (10 ** i)-1 and n <= (10 ** (i+1))-1:
            print((n//10**(i-2)) * (10**(i-2)))
            break