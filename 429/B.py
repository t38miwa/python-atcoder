# 長さ4の整数列A = [3 2 3 4]と整数10が与えられる
# Aの4個の要素から１個取り除くことで残りの3個の要素の和をちょうどMにできるか判定して

N,M = map(int,input().split())
A = list(map(int,input().split()))

for i in range(N):
    temp_A = A.copy()
    temp_A[i] = 0
    if sum(temp_A) == M:
        print('Yes')
        exit()
print('No')