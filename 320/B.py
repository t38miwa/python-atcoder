s=input()

result=''
for i in range(len(s)+1):
    for j in range(len(s)+1):
        string=s[i:j]
        if string == string[::-1] and len(string)>len(result):
            result=string

print(len(result))