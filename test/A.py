# Nが与えられる
# 各文字が奇数回しか現れないように文字を出力する
# N = 4ならcodeを返す
# 26以上だと文字を複数回表示しないといけない
# Nが奇数ならaをN個出力、Nが偶数ならaをN-1個、bを一個出力する

def solution(N):
    if N % 2 == 1:
        return 'a' * N
    else:
        return 'a' * (N-1) + 'b'

N = int(input())
print(solution(N))