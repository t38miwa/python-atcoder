p,q=input().split()

dis=[3,1,4,1,5,9]

abc=['A','B','C','D','E','F','G']

p_index=0
q_index=0
sum=0
for i in range(len(abc)):
    if p==abc[i]:   
        p_index=i
    elif q==abc[i]:   
        q_index=i

if p_index<q_index:
    for i in range(p_index,q_index):
        sum+=dis[i]
else:
    for i in range(q_index,p_index):
        sum+=dis[i]

print(sum)