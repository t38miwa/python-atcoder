N = int(input())

water = 0
prev_T = 0
for i in range(N):
    T,V = map(int,input().split())
    water -= (T - prev_T)
    if water < 0:
        water = 0
    water += V
    prev_T = T

print(water)