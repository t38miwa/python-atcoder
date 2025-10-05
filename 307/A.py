N=int(input())
A=list(map(int,input().split()))

week_sums=[]
for i in range(N):
    week_sum=sum(A[i*7:(i+1)*7])
    week_sums.append(week_sum)

print(' '.join(map(str, week_sums)))