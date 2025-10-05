S=list(input())

if S[0]!='<':
    print('No')
    
elif S[-1]!='>':
    print('No')

else:
    for i in range(1,len(S)-1):
        if S[i]!='=':
            print('No')
            break

    else:
        print('Yes')