N=int(input())
S=input()
S_list=list(S)

count_T=0
count_A=0

for i in range(N):
    if S_list[i]=="T":
        count_T+=1  
    elif S_list[i]=="A":
        count_A+=1

    if count_T>count_A and count_T-1==count_A:
        result='T'
    elif count_A>count_T and count_A-1==count_T:
        result='A'

if count_T>count_A:
    print('T')
elif count_A>count_T:
    print('A')
else:
    print(result)