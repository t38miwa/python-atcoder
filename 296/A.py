N=int(input())
S=input()
S_list=list(S)

for i in range(N-1):
    if S_list[i]==S_list[i+1]:
        print("No")
        break
else:
    print("Yes")