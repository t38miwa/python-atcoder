list=[]

while True:
    n=int(input())
    list.insert(0,n)
    if n==0:
        break

for i in range(len(list)):
    print(list[i])