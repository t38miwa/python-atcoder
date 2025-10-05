S = input()

result = 0
# 2を見つける
for i in range(len(S)):
    if S[i] == '2':
        result += 1

print('2'*result)