"""AtCoder Beginner Contest 332 B"""
k, g, m = map(int, input().split())
rg = 0
rm = 0
for i in range(k):
    if rg == g:
        rg = 0
    elif rm == 0:
        rm = m
    else:
        t = g - rg
        if rm <= t:
            rg += rm
            rm = 0
        else:
            rg = g
            rm -= t

print(rg, rm)