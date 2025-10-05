

N = int(input())

count = 0
is_login = False
for i in range(N):
    S = input()
    # ログインしてない、private
    if S == 'login':
        is_login = True
    if S == 'logout':
        is_login = False
    
    if is_login == False:
        if S == 'private':
            count += 1

print(count)