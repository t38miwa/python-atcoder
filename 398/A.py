N = int(input())

if N == 1:
    print('=')
    exit()

if N == 2:
    print('==')
    exit()

mid_index = N // 2
# 基本-でmid_indexだけ=にする
result_str = ['-']*N
if N % 2 == 0:
    result_str[mid_index] = '='
    result_str[mid_index-1] = '='
else:
    result_str[mid_index] = '='

print(''.join(result_str))