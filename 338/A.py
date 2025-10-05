S = input()

# 先頭の文字が大文字で、残りの文字がすべて小文字かどうかを判定
if S[0].isupper() and S[1:].islower():
    print("Yes")
else:
    print("No")
