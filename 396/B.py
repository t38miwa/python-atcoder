Q = int(input())

yama = [0]*100
for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 2:
        popped_item = yama.pop(-1)
        print(popped_item)
    else:
        yama.append(query[1])