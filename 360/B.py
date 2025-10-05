s,t=input().split()

s_len=len(s)

for w in range(1,s_len):
    for c in range(w):
        temp=""
        index=c
        while index < s_len:
            temp+=s[index]
            index += w
        if temp == t:
            result=True

print("Yes" if result else "No")