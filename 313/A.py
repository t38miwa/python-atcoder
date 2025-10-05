N = int(input())
if N == 1:
    print(0)
    exit()
p1, *p = map(int, input().split())
ans = max(max(p) + 1 - p1, 0)
print(ans)

