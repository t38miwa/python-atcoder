s=input()
alpha=[0]*26

for i,ch in enumerate(s):
    alpha[ord(ch)-ord('a')]+=1


max=0
index=0
for i in range(26):
    if alpha[i]>max:
        max=alpha[i]
        index=i

print(chr(ord('a')+index))