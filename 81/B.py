N = int(input())
A = list(map(int,input().split()))

count = 0
result = True
# -が行えなくなるまで操作するパターンはwhileを使うことが多い
while result == True:
    # 現在のAの配列の全ての整数が偶数であることを確認する
    for i in range(N):
        result = True
        #  もし2で割ることができなければresultをFalseに設定し、回数を出力して終了する
        if A[i]%2 != 0:
            result = False
            print(count)
            break
    
    for i in range(N):
        A[i] = A[i]//2
    count += 1