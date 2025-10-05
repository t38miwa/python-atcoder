S = input()

result = []
count = 0
for i in range(1,len(S)):
    if S[i] == '-':
        count += 1
    if S[i] == '|':
        result.append(str(count))
        count = 0

print(*result)