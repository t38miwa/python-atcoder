# 長さ5の数列A=[1 2 4 8 16]と1以上5以下の整数3が与えられる。
# 長さ3の連続する部分列が5-3+1=3個ある

n,k = map(int,input().split())
a = list(map(int,input().split()))

# 配列Aに対して、配列S
s = [0] * (n+1)
for i in range(n):
    s[i+1] = s[i] + a[i]
print(s)

ans = 0
for i in range(n-k+1):
    ans += s[i+k] - s[i]
    print(s[i+k] - s[i])
    print(ans)
print(ans)