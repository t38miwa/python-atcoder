N = int(input())

G = [list('#'*N) for _ in range(N)]
print(G)

for i in range(5,1,-1):
    if i % 2 == 0:
        for j in range(i):
            print('#'*5)


print(G)