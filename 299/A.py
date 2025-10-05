N=int(input())

S=input()
S_list=list(S)

bou_index=[]
kome_index=0

for i in range(N):
    if S_list[i]=="|":
        bou_index.append(i)
    if S_list[i]=="*":
        kome_index=i

if bou_index[0]<kome_index<bou_index[1]:
    print("in")
else:
    print("out")