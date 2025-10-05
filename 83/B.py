N,A,B = map(int,input().split())
total = 0

for i in range(1,N+1):
    digit_sum = 0
    temp = i
    # 例：20が0になるまで
    while temp > 0:
        # 20÷10のあまり、0をdigit_sumに加算
        # 2÷10のあまり、2をdigit_sumに加算
        digit_sum += temp % 10
        # temp = 2になる
        # 2÷10 = 0でwhile文を抜ける
        temp //= 10
    # digit_sumは現在2なので、2以上5以下の条件に当てはまる
    if A <= digit_sum <= B:
    # 20を合計値に加算する
        total += i
print(total)