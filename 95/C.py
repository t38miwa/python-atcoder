# Aピザ= 1500円、Bピザ= 2000円、ABピザ= 1600円、3枚、２枚用意する必要あり
# 入力例1の場合、基本的にABピザを優先して買うべき、安いから
# 同量まではABピザで購入し、不足分をそれぞれでかうという方針
# A,Bの平均値段が、ABの値段より高い時は上の方針がいい

A,B,C,X,Y = map(int,input().split())

avg = (A + B) // 2
# そのまま買うパターン
if avg < C:
    direct = (X * A) + (Y * B)
    print(direct)
    exit()
# ABをmax分買うパターン
else:
    max_ab = max(X,Y) * C * 2
# ABをmin分買うパターン
    min_ab = min(X,Y) * C * 2
    if X > Y:
        min_ab += (X-Y) * A
    else:
        min_ab += (Y-X) * B
    print(min(max_ab,min_ab))