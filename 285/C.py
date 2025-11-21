# A=65
# Z=90

# A=1
# C=3
# Z=26
# AA=27
# AZ=AA+25=52
# BA=53
# BZ=78
# ZA=26×26+1
# ZZ=26×26+26
# AAA=702
# AAC=55

# A=1 26xx0+1
# Z=26
# AA=27 26xx1+1
# AZ=52
# ZA=677 26x26+1
# ZZ=702 26x26+26
# AAA=703 26xx2+26x1+1
# AAA=703 (26xx2)x1+(26xx1)x1+(26xx0)x1
# AAZ=728 (26xx2)x1+(26xx1)x1+(26xx0)x26
# AZA=    (26xx2)x1+(26xx1)x26+(26xx0)x1
# AAAA=26xx3+26xx2+26xx1+1
S = input()

# 文字を数字に変換する関数
def toInt(s):
    return ord(s)-64

# 26*Zの数字＋
ans = 0
for i in range(len(S)):
    ans += 26 ** (len(S)-(i+1)) * toInt(S[i])
print(ans)