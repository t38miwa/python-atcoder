n, m = map(int, input().split())
a = list(map(int, input().split()))

s = 0
for i, a_i in enumerate(a):
    s += a_i
    if s > m:
        print(i)
        exit()

print(n)
