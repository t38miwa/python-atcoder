N = int(input())

c_list = []
l_list = []
for i in range(N):
    c,l = input().split()
    l = int(l)
    c_list.append(c)
    l_list.append(l)

result = []
if sum(l_list) > 100:
        print('Too Long')
        exit()

result = []
for i in range(N):
    result.append(c_list[i]*l_list[i])
print(''.join(result))