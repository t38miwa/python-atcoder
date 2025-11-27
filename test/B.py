# 長さN=6のS = "011100"が与えられる
# 非負数 v=28を二進数表記にエンコードしたのがS
# 2つの種類の操作がその値を修正するために行われる
# vが奇数なら-1する
# vが偶数なら/2する
# この操作がvが0になるまで行われる
# 入力例なら7回の操作で0になる
# 0になるまで繰り返す必要のある操作回数を返す

# ある整数を0にするまでに必要な操作数
# Nは10**6
# 愚直に実装するならwhile文でVが0になるまで２種類の操作を繰り返し、その回数をansとしてreturnすればいい

def solution(S):
    subtract_cnt = 0
    for s in S:
        if s == '1':
            subtract_cnt += 1
    # 二進数の先頭は1になるようにする
    first_one = S.find('1')
    bit = len(S) - first_one
    divide_cnt = bit - 1
    
    return subtract_cnt + divide_cnt

S = input()
print(solution(S))