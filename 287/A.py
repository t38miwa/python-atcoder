N=int(input())

countFor=0
countAgainst=0
for i in range(N):
    S=input()
    if S=="For":
        countFor+=1
    if S=="Against":
        countAgainst+=1

if (N/2)<=countFor:
    print("Yes")
else:
    print("No")