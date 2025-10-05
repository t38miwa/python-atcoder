N = int(input())
A = list(map(int, input().split()))

# 等比数列の判定
# すべての隣接する要素の比が等しいかチェック

if N <= 1:
    print('Yes')
else:
    # 公比を計算（分数として扱う）
    from fractions import Fraction
    
    # 最初の比を計算
    if A[0] == 0:
        # 最初の要素が0の場合、すべて0でないと等比数列にならない
        if all(x == 0 for x in A):
            print('Yes')
        else:
            print('No')
    else:
        ratio = Fraction(A[1], A[0])
        
        # すべての隣接する要素の比が等しいかチェック
        is_geometric = True
        for i in range(1, N):
            if A[i] == 0:
                # 0が含まれる場合の特別処理
                if A[0] == 0:
                    # 最初が0なら、すべて0でないと等比数列にならない
                    if not all(x == 0 for x in A):
                        is_geometric = False
                        break
                else:
                    # 最初が0でないのに0が現れたら等比数列ではない
                    is_geometric = False
                    break
            else:
                current_ratio = Fraction(A[i], A[i-1])
                if current_ratio != ratio:
                    is_geometric = False
                    break
        
        if is_geometric:
            print('Yes')
        else:
            print('No')