# AtCoder用のPythonテンプレート
# コンテスト番号: 75

# よく使う変数の初期化
ay, an, G, tr, fa = 'Yes', 'No', {}, True, False
flg, cnt, pos, rec = tr, 0, 0, []

# 入力の読み込み（必要に応じてコメントアウトを外す）
# N = int(input())
# S = input()
# A = list(map(int, input().split()))
# N,M = map(int,input().split())
# lst = [i+1 for i in range(n)]

H,W = map(int,input().split())
S = [['@']*(W+2)] + [['@']+list(input())+['@'] for _ in range(H)] + [['@']*(W+2)]
for i in range(H+2):
    for j in range(W+2):
        if S[i][j] == '.':
            S[i][j] = 0


for i in range(H+2):
    for j in range(W+2):
        if S[i][j] == '#':
            for x in range(i-1,i+2):
                for y in range(j-1,j+2):
                    if S[x][y] != '@' and S[x][y] != '#':
                        S[x][y] += 1

for i in range(H+1):
    result = []
    for j in range(W+1):
        if S[i][j] != '@':
            result.append(str(S[i][j]))
    print("".join(result))
# よく使う入力パターン
# A = [int(input()) for _ in range(n)]
# A = [list(map(int, input().split())) for _ in range(n)]
# A = [list(map(int, list(input()))) for _ in range(n)]
# X, Y = [list(i) for i in zip(*[list(map(int, input().split())) for _ in range(n)])]

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
