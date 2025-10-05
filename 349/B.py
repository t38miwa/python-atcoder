s=input()

result={}
for i in range(len(s)):
    if s[i] in result:
        result[s[i]]+=1
    else:
        result[s[i]]=1

freq = {}
for count in result.values():
    if count in freq:
        freq[count] += 1
    else:
        freq[count] = 1
for ans in freq.values():
    if ans != 0 and ans != 2:
        print('No')
        break

else:
    print('Yes')