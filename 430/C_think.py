# 4分以上運転するなら2分以上休憩を取る必要がある
# 長さ11の文字列
# 1<= l <= r <= 11
# Sのlからr文字目までに含まれるaの個数が4以上
# Sのlからr文字目までに含まれるbの個数がB未満

N,A,B = map(int,input().split())
S = input()

sum_a = [0] * (N+1)
sum_b = [0] * (N+1)

for i in range(N):
    sum_a[i+1] = sum_a[i] + (1 if S[i] == 'a' else 0)
    sum_b[i+1] = sum_b[i] + (1 if S[i] == 'b' else 0)

# 二分探索で r_min_a (cnt_a >= A を満たす最小のr) を求める
def find_r_min_a(l):
    left, right = l, N - 1
    result = N  # 見つからない場合はN
    while left <= right:
        mid = (left + right) // 2
        cnt_a = sum_a[mid + 1] - sum_a[l]
        if cnt_a >= A:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result

# 二分探索で r_max_b (cnt_b < B を満たす最大のr) を求める
def find_r_max_b(l):
    left, right = l, N - 1
    result = l - 1  # 見つからない場合はl-1
    while left <= right:
        mid = (left + right) // 2
        cnt_b = sum_b[mid + 1] - sum_b[l]
        if cnt_b < B:
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    return result

# 各lについて条件を満たすrの個数を合計
ans = 0
for l in range(N):
    r_min_a = find_r_min_a(l)
    r_max_b = find_r_max_b(l)
    if r_min_a <= r_max_b:
        ans += r_max_b - r_min_a + 1

print(ans)
