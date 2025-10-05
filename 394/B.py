N = int(input())
S_list = []
len_list = []

s_dic = {}
for i in range(N):
    S = input()
    s_dic[S] = len(S)
    
sorted_by_key = dict(sorted(s_dic.items(), key=lambda x: x[1]))
result = []

for s_key in sorted_by_key:
    result.append(s_key)

print(''.join(result))