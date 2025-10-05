N=int(input())
S=input()
S_list=list(S)

count_o=0
count_x=0

for i in range(N):
    if S_list[i]=="x":
        count_x+=1
    elif S_list[i]=="o":
        count_o+=1

if (count_o>=1)and(count_x==0):
    print("Yes")
else:
    print("No")
