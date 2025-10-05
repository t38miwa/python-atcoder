s=input()
result=[]

for i in range(len(s)+1):
    for j in range(1,len(s)+1):
            if s[i:j] not in result and s[i:j]!='':
                result.append(s[i:j])

print(len(result))