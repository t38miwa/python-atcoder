N = int(input())

# 00001を左に5ずらす=2^5=32
for bit in range(1 << N):
    subset = []
    for i in range(N):
        # bit = 00011, 1を左に0ずらす=00001　この２つの値のand演算の結果= 00000　0ならfalse,それ以外はtrue
        if bit & (1 << i):  # i番目の要素が含まれているか判定
            subset.append(i)
    print(bit,i,subset)