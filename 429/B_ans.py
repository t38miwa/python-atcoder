n, m = map(int, input().split())
a = list(map(int, input().split()))
if sum(a) - m in a:
    print("Yes")
else:
    print("No")