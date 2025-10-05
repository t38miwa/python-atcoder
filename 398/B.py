A = list(map(int,input().split()))

# {カードの数字：枚数}という辞書を作り、3以上の１種類のカード、２以上の１種類のカードがあるかを調べる
# 枚数をカウントする
dic = {}
for a in A:
    if a in dic:
        dic[a] += 1
    else:
        dic[a] = 1

sorted_by_key = dict(sorted(dic.items(), key=lambda x: x[1],reverse=True))



# 3以上の１種類のカード、２以上の１種類のカードがあるかを調べる
flag1 = False
flag2 = False
# 辞書のvaluesの１つ目を取り出したい
if len(sorted_by_key) == 1:
    print('No')
    exit()
if list(sorted_by_key.values())[0] >= 3:
    flag1 = True
if list(sorted_by_key.values())[1] >= 2:
    flag2 = True

if flag1 and flag2:
    print('Yes')
else:
    print('No')