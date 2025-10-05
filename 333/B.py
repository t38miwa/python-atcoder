s=input()
t=input()

type1=2
diff1=abs(ord(s[0])-ord(s[1]))
if diff1 in (1,4):
    type1=1

type2=2
diff1=abs(ord(t[0])-ord(t[1]))
if diff1 in (1,4):
    type2=1

print("Yes" if type1 == type2 else "No")