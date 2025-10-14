N, M = map(int, input().split())
lamps = [list(map(lambda x:int(x)-1, input().split()))[1:]
         for _ in range(M)]
p = list(map(int, input().split()))

ans = 0

# ビット全探索で全ての電球が点灯する組み合わせを見つける
for bit in range(1 << N):
    for i in range(M):
        on_sum = 0
        for j in range(N):
            if bit >> j & 1 and j in lamps[i]:
                on_sum += 1
        if on_sum % 2 != p[i]:
            break
    else:
        ans += 1

print(ans)