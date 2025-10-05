S=input()

if int(S[3:])>=350:
    print('No')
elif int(S[3:])==316:
    print('No')
elif int(S[3:])<350 and not int(S[3:])==0:
    print('Yes')
elif int(S[3:])==0:
    print('No')