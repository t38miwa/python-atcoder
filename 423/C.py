N,R = map(int,input().split())
L = list(map(int,input().split()))

# 閉操作の後に開操作を行うことはない
# 閉操作の回数＝開く操作の回数＋始めに開いていた鍵の個数の和
if(L.count(0) == 0):
  # 何もしなくていい
  print(0)
  exit()

x = 0
y = 0
for i in range(N):
    if L[i] == 0:
        x = i
        break

for i in reversed(range(N)):
    if L[i] == 0:
        y = i
        break

mi = min(x,R)

ma = max(y+1,R)

target = L[mi:ma]

ans = target.count(1) + len(target)

print(ans)