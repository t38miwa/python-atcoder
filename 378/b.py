N = int(input())
# 日付÷q = 答え　あまりr の日にゴミは収集される
data = []
for i in range(N):
    q,r = map(int,input().split())
    data.append((q,r))
    # 10日にゴミ1回収される（10/7=1あまり3）
Q = int(input())
for i in range(Q):
    t,d = map(int,input().split())
    # 
    for j in range(d,d + data[t-1][0]):
        #print(q[t-1],r[t-1])
        if j % data[t-1][0] == data[t-1][1]:
            print(j)
            break