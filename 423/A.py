X,C = map(int,input().split())

# 常に引き出し額＋手数料がX以下である必要がある

for i in range(0,X,1000):
    total = i + (i//1000)*C
    if X-C < 1000:
        print(0)
        exit(0)
    if total <= X:
        result = i

print(result)