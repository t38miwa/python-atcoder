subtract_cnt = 0
    for s in S:
        if s == '1':
            subtract_cnt += 1
    # 二進数の先頭は1になるようにする
    first_one = S.find('1')
    bit = len(S) - first_one
    divide_cnt = bit - 1
    
    return subtract_cnt + divide_cnt