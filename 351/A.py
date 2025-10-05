A=list(map(int,input().split()))
B=list(map(int,input().split()))

sum_A=0
sum_B=0

for i in range(9):
    sum_A+=A[i]

for i in range(8):
    sum_B+=B[i]

print(sum_A-sum_B+1)