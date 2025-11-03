# 3行3列からなるグリッド、#なら黒、.なら白
# 2行2列を取り出す方法はいくつある

N,M = map(int,input().split())
S = [list(input()) for _ in range(N)]

# resultというリストに組み合わせを保存する
results = []
for k in range(N-M):
    for j in range(N-1):
        result = []
        for i in range(N-1):
            result.append(S[i+k][j:j+M])
        if result not in results:
            results.append(result)
        print(result)
print(len(results))
