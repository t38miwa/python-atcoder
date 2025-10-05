S=list(map(int,input().split()))

for i in range(len(S)-1):
    if S[i]>S[i+1]:
        print('No')
        break
    elif 100>S[i] or S[i]>675:
        print('No')
        break
    elif S[i] % 25 != 0:
        print('No')
        break

else:
    print('Yes')