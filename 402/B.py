Q = int(input())

# [3,1,15,3]のようにメニュー番号を管理する。
menu = []
# 2の時にmenu[0]をpopする
for i in range(Q):
    query = list(map(int,input().split()))
    if query[0] == 1:
        menu.append(query[1])
    if query[0] == 2:
        popped_menu = menu.pop(0)
        print(popped_menu)