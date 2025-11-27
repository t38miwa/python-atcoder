def solution(blocks):
    n = len(blocks)

    # 左方向にどこまで行けるか
    left = [0] * n
    left[0] = 0
    for i in range(1, n):
        if blocks[i] >= blocks[i - 1]:
            left[i] = left[i - 1]
        else:
            left[i] = i

    # 右方向にどこまで行けるか
    right = [0] * n
    right[n - 1] = n - 1
    for i in range(n - 2, -1, -1):
        if blocks[i] >= blocks[i + 1]:
            right[i] = right[i + 1]
        else:
            right[i] = i

    # 最大距離を計算
    ans = 1
    for i in range(n):
        distance = right[i] - left[i] + 1
        ans = max(ans, distance)

    return ans

blocks = list(map(int,input().split()))
print(solution(blocks))