# ①問題文を理解する
# ②解法のステップをコメントで記載
# ③コードに落とし込んでいく
# ④分解が足りない場合は追加でコメントを記載し、②、③を繰り返す

#Nの階乗が入力Xになるような正整数Nを求める
X = int(input())

# 1,Xまでの数でfor文を回して、その数の階乗がXになるか調べる
result = 1
for i in range(1,X+1):
    result *= i
    if result == X:
        print(i)
        break