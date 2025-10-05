s = {1, 2, 3} - set(map(int, input().split()))
if len(s) == 1:
    ans = s.pop()
    print(ans)
else:
    print(-1)
