S,A,B,X = map(int, input().split())

# X // (A+B)完全なサイクルの回数
# S * A　１サイクルで走る距離
print(X // (A+B) * S * A + min(A, X % (A+B)) * S)