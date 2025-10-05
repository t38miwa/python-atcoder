N = int(input())
list = []
for _ in range(N):
    T,X,Y = map(int,input().split())
    list.append((T,X,Y))

flag = True
prev_time, prev_x, prev_y = 0,0,0
for T,X,Y in list:
    distance = abs(X - prev_x)+abs(Y - prev_y)
    time = (T - prev_time)
    if (distance > time) or ((time - distance)%2 != 0):
        flag = False
        break
    prev_time, prev_x, prev_y = T,X,Y

if flag:
    print('Yes')
else:
    print('No')