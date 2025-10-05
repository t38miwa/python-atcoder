import math

N = int(input())

sum = 0
prev_x = 0
prev_y = 0
for i in range(N):
    X,Y = map(int,input().split())
    sum += math.sqrt((prev_x - X)**2 + (prev_y - Y)**2)
    prev_x = X
    prev_y = Y

sum += math.sqrt((prev_x - 0)**2 + (prev_y - 0)**2)
print(sum)