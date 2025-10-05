N=list(map(int,input().split())) #連続した数字の入力を受け付ける時の処理

for i in range(len(N)-1):
    if N[i]!=N[i+1]+1:
        print('No')
        break
    
else:
    print('Yes')
