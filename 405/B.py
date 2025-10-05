N,M = map(int,input().split())
A = list(map(int,input().split()))

count = 0

check_A = {i for i in range(1,M+1)}

for i in range(N+1):
# set型にし、それがA_setと同じか確かめる
    if check_A != set(A):
        print(count)
        exit()
# Aの末尾の要素を削除する
    A.pop(-1)
    count += 1