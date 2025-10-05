n, l, r = map(int, input().split())

ans = [i for i in range(1, l)] + [i for i in range(r, l - 1, -1)] + [i for i in range(r + 1, n + 1)]

print(*ans)
