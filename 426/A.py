X,Y = input().split()

# indexがどちらが先か調べる
os = ["Ocelot", "Serval", "Lynx"]

x_index = 0
y_index = 0
for i in range(3):
    if X == os[i]:
        x_index = i
    if Y == os[i]:
        y_index = i

if x_index >= y_index:
    print('Yes')
else:
    print('No')