# A = [0 1 0 1 1]が与えられれている
# これは道路上を走る連続した車を表す
# 0は右、1は左

# ある特定のインデックスまでの1の数を保持する累積和リストを作る
# 0があるindexを発見し、そのindexの累積和をansに追加する
# 全体の1の数 - そのindexの1の数

def solution(A):
    ans = 0
    # Aの累積和配列を作成する
    S = [0] * (len(A)+1)
    for i in range(len(A)):
        S[i+1] = S[i] + A[i]
    # 0があるindexを発見
    for i in range(len(A)):
        if A[i] == 0:
            # 全体の1の数 - そのindexの1の数
            ans += S[-1] - S[i+1]
    if ans >= 10**9:
        return -1
    else:
        return ans

A = list(map(int,input().split()))
print(solution(A))