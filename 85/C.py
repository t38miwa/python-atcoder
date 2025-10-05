N,Y = map(int,input().split())

# for文の三重ループを回せばすぐ解ける問題、だが、そうなると最大値の2000^3で１億回を超えるため、制限内に計算実行できない
flag = False
for x in range(N+1):
    if flag:
        break
    for y in range(N+1):
# a+b+c = Nなのでc = N - a - bで求められる。これによって二重ループで済む
        z = N - x - y
        if (z >= 0) and (x + y + z == N) and (10000*x + 5000*y + 1000*z == Y):
            print(x,y,z)
            flag = True

if flag == False:
    print(-1,-1,-1)