# AtCoder用のPythonテンプレート
# コンテスト番号: 418

# tの先頭、末尾がtで長さが３以上、tに含まれるtの数がx
t = list(input())

t_list = []
# tの部分文字列を配列にappendする
for i in range(len(t)):
    for j in range(i+1,len(t)):
        if t[i] == 't' and t[j] == 't':
            if len(t[i:j+1]) >= 3:
                t_list.append(t[i:j+1])


# 部分文字列の充填率を返す関数を作成
def fullfil(S):
    x = 0
    for i in range(len(S)):
        if S[i] == 't':
            x += 1  
    formatted_result = (x-2)/(len(S)-2)
    return formatted_result

result = 0
for i in range(len(t_list)):
    num = fullfil(t_list[i])
    if num >= result:
        result = num

print(result)


# よく使う変数の初期化
ay, an, G, tr, fa = 'Yes', 'No', {}, True, False
flg, cnt, pos, rec = tr, 0, 0, []

# 入力の読み込み（必要に応じてコメントアウトを外す）
# n = int(input())
# s = input()
# a = list(map(int, input().split()))
# lst = [i+1 for i in range(n)]

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
