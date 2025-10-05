S=input()
S_list=list(S)

for i in range(0,len(S_list)-1,2):
    S_list[i],S_list[i+1]=S_list[i+1], S_list[i]

print("".join(S_list))