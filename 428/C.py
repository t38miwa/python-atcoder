# (ではじまり、)で終わる部分文字列を削除して空文字にすることができる　＝　Tを良い括弧列
# Q個のクエリがあり、処理後にSが良い括弧列か判定する
# 
def is_good(S):
    while len(S) >= 2:
        if '()' in S:
            S = S.replace('()','')
        else:
            break  
    if len(S) > 0:
        return False
    else:
        return True

Q = int(input())
S = []
for i in range(Q):
    query = input().split()
    if query[0] == '1':
        S.append(query[1])
    if query[0] == '2':
        S.pop(-1)
    flag = is_good(''.join(S))
    print('Yes' if flag else 'No')