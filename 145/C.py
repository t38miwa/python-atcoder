# 3個の町、町1は(0,0)に位置している
import itertools
import math

N = int(input())

point = []

for _ in range(N):
    xy = list(map(int,input().split()))
    point.append(xy)

num = list(range(N))

ptn = list(itertools.permutations(num))

sum_dist = 0

def dist(a,b):
    x1 = point[a][0]
    y1 = point[a][1]
    x2 = point[b][0]
    y2 = point[b][1]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

for p in ptn:
    for i in range(N-1):
        a = p[i]
        b = p[i+1]
        sum_dist += dist(a,b)

print(sum_dist/len(ptn))