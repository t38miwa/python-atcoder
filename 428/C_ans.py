# 開き括弧と閉じ括弧の数が同じである必要がある
# 文字列Sのどの点においても閉じ括弧が開き括弧より多くならないこと
# この条件を満たせば良い文字列

Q = int(input())
A = [0]
B = [0]
for i in range(Q):
    query = input().split()
    if query[0] == '1':
        new_A = A[-1] + (1 if query[1] == '(' else -1)
        new_B = min(B[-1],new_A)
        A.append(new_A)
        B.append(new_B)
    else:
        A.pop()
        B.pop()
    if A[-1] == 0 and B[-1] == 0:
        print('Yes')
    else:
        print('No')