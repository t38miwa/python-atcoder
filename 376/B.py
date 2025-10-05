"""AtCoder Beginner Contest 376 B"""
n, q = map(int, input().split())

L = 1
R = 2
result = 0
for i in range(q):
    h, t = input().split()
    t = int(t)

    if h == 'L':
        if L < t:
            if L < R < t:
                result += L + n - t
            else:
                result += t - L
        else:
            if t < R < L:
                result += t + n - L
            else:
                result += L - t
        L = t
    else:
        if R < t:
            if R < L < t:
                result += R + n - t
            else:
                result += t - R
        else:
            if t < L < R:
                result += t + n - R
            else:
                result += R - t
        R = t

print(result)