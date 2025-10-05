S = input()

result = []
# 大文字か判定し、大文字ならresult_listにappend
for i in range(len(S)):
    if S[i].isupper():
        result.append(S[i])

print(''.join(result))