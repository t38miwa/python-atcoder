S = input()[::-1]

words = ["dream", "dreamer", "erase", "eraser"]
# 先頭から処理するとprefixの関係になるため、並びを逆にする
words = [word[::-1] for word in words]


while len(S) > 0:
    matched = False
    for word in words:
        if S.startswith(word):
            # マッチしたらその単語分だけ、文字列を削除
            S = S[len(word):]
            matched = True
            break
    if not matched:
        break

if len(S) == 0:
    print("YES")
else:
    print("NO")