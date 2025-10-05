a = list(map(int,input().split()))

color = {0:0,1:0,2:0,3:0,4:0}
for i in range(4):
# もしaの１番目が1だったらcolorの１番目のvalueに1を加算
    if a[i] == 1:
        color[1] += 1
    if a[i] == 2:
        color[2] += 1
    if a[i] == 3:
        color[3] += 1
    if a[i] == 4:
        color[4] += 1

result = 0
for i in range(5):
    result += color[i] // 2

print(result)