A,B,C,D = map(int,input().split())
list = [A,B,C,D]

dic = {}
result = True

for i in range(4):
    if list[i] in dic:
        dic[list[i]] += 1
    else:
        dic[list[i]] = 1

if len(dic) == 2:
    print('Yes')
else:
    print('No')