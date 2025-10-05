N=int(input())

str=[]
for i in range(N):
    S=input()
    str.append(S)

for i in range(len(str),-1,-1):
    print(str[i])