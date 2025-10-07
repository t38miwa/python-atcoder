# AtCoder用のPythonテンプレート
# コンテスト番号: 419

# よく使う変数の初期化
ay, an, G, tr, fa = 'Yes', 'No', {}, True, False
flg, cnt, pos, rec = tr, 0, 0, []

# 入力の読み込み（必要に応じてコメントアウトを外す）
# n = int(input())
# s = input()
# a = list(map(int, input().split()))
# lst = [i+1 for i in range(n)]

Q = int(input())
bag = []
for i in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 1:
        bag.append(q[1])
    if q[0] == 2:
        sorted_bag = sorted(bag)
        print(sorted_bag[0])
        bag.remove(sorted_bag[0])
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
