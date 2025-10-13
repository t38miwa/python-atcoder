# f(123)=1+2+3=6を計算する関数
def f(x):
    return sum(map(int,str(x)))

N = int(input())

A = [1]
for i in range(N):
    x = sum(A)
    # A5=16のf(16)=7であることを求める
    ans = f(x)
    A.append(ans)
print(x)