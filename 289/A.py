s=input().strip()

result=[]
for  char in s:
    if char=="1":
        result.append("0")
    if char=="0":
        result.append("1")
print(''.join(result))