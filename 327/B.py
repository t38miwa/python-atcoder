b=int(input())

result=-1
for i in range(1,100):
    if i**i==b:
        result=i
        break
print(result)