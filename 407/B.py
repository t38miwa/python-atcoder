# 分母は36
# 出目の合計が10以上 4,6 5,5 5,6 6,4 6,5 6,6
X,Y = map(int,input().split())

result = []
for x in range(1,7):
    for y in range(1,7):
        if x+y >= X:
            result.append((x,y))
        if abs(x-y) >= Y:
            if (x,y) not in result:
                result.append((x,y))
print(len(result)/36)
# print((count_x+count_y)/36)