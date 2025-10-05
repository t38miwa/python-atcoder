def count_full_moon_days(N, M, P):
    if M > N:
        return 0  # 最初の満月の日が範囲を超えている場合は0を返す
    # 満月の日数を求める
    return (N - M) // P + 1

# 入力を受け取る
N, M, P = map(int, input().split())

# 満月を見られる日の数を出力
print(count_full_moon_days(N, M, P))
