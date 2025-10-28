# 整数10000が与えられる
# A,Bに対してF(A,B)は10進数表記における、Aの桁数の大きい方と定義する
import math
N = int(input())
n = int(math.sqrt(N))

# A*BがNとなる組み合わせを考え、それの桁数の大きい方の数が最小であるものを求める
ans = 11
for a in range(1,n+1):
    if N % a == 0:
        b = N // a
        result = len(str(b))
        if result < ans:
            ans = result
print(result)