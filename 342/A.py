S=list(input())

result=0
for i in range(len(S)-2):
    if S[i]!=S[i+1] and S[i]==S[i+2]:
        result=i+1
    elif S[i]!=S[i+1] and S[i+1]==S[i+2]:
        result=i 
    elif S[i]==S[i+1] and S[i+1]!=S[i+2]:
        result=i+2
        
print(result+1)