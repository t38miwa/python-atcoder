# AtCoder用のPythonテンプレート
# コンテスト番号: 420
# 人がN人、M回の投票

# よく使う変数の初期化
ay, an, G, tr, fa = 'Yes', 'No', {}, True, False
flg, cnt, pos, rec = tr, 0, 0, []

# 入力の読み込み（必要に応じてコメントアウトを外す）
# n = int(input())
# s = input()
# a = list(map(int, input().split()))
# lst = [i+1 for i in range(n)]
N,M = map(int, input().split())
S = [list(input()) for _ in range(N)]

counts = [0] * N
for j in range(M):
    result = []
    for i in range(N):
        result.append(int(S[i][j]))

    x = result.count(0)
    y = result.count(1)
    for k in range(N):
        if x == 0 or y == 0:
            counts[k] += 1
        elif x < y:
            if result[k] == 0:
                counts[k] += 1
        else:
            if result[k] == 1:
                counts[k] += 1

final = []
huge = max(counts)
for i in range(len(counts)):
    if counts[i] == huge:
        final.append(i+1)
print(*final)

# よく使う入力パターン
# a = [int(input()) for _ in range(n)]
# a = [list(map(int, input().split())) for _ in range(n)]
# a = [list(map(int, list(input()))) for _ in range(n)]
# x, y = [list(i) for i in zip(*[list(map(int, input().split())) for _ in range(n)])]

# xy = [list(map(int, input().split())) for _ in range(n)]
# x, y = [list(i) for i in zip(*xy)]

# 文字列処理
# for i in range(len(txt)):
#     ary.append(list(txt[i]))

# アルファベット変換
# A-Z：65 - 90　a-z：97 - 122　ord/chr

# デバッグ用
# print("debug:", variable_name)

# メイン処理
# ここにコードを書く

# 出力
# print(result)
