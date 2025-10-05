S = input()
T = input()

if S == T:
    print(0)
else:
    if len(S) == len(T):  
        for i in range(len(S)):
            if S[i] != T[i]:
                print(i+1)
                exit()
    if len(S) < len(T):  
        for i in range(len(S)):
            if S[i] != T[i]:
                print(i+1)
                exit()
        print(len(S)+1)
        exit()
    if len(S) > len(T):  
        for i in range(len(T)):
            if T[i] != S[i]:
                print(i+1)
                exit()
        print(len(T)+1)
        exit()