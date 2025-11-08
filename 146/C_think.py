A, B, X = map(int, input().split())

def check(x):
    dx = len(str(x))
    return A * x + B * dx

ok = 0
ng = 1000000001

while ok + 1 != ng:
    md = (ok + ng) // 2
    if check(md) <= X:
        ok = md
    else:
        ng = md

print(ok)
