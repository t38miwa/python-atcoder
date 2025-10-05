K=int(input())

result = ""
for i in range(K):
    result += chr(ord('A') + i)

print(result)

#ordはunicodeを返す
#chrはunicodeを文字列に変換
#A=65+1で66、それはBなのでその文字をresultに格納