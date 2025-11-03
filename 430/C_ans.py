import bisect 

N,A,B = map(int,input().split())
S = input()

sum_A = [0] * (N+1)
sum_B = [0] * (N+1)

for i in range(N):
    sum_A[i+1] = sum_A[i] + (1 if S[i] == 'a' else 0)
    sum_B[i+1] = sum_B[i] + (1 if S[i] == 'b' else 0)
print(sum_A)
print(sum_B)

ans = 0
for l in range(N):
    r_a = bisect.bisect_left(sum_A, sum_A[l] + A)
    r_b = bisect.bisect_left(sum_B, sum_B[l] + B)
    print(l,r_a,r_b)
    ans += max(r_b - r_a, 0)

print(ans)