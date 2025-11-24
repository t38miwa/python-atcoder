# 2個の長さ3の .,T からなる文字列TTTとT.Tが与えられる
# iは1-2,jは1-2を満たす整数
# TTTの2番目の文字も3番目の文字もTであるようなものを選ぶ
# TTTの2文字目をPで置き換え、3文字目をCで置き換える
# 結果TPCとなる

H,W = map(int,input().split())

# ある文字列の1からW-1文字において、TTTの2番目の文字も3番目の文字もTであるようなものを選ぶ
for i in range(H):
    S = list(input())
    for j in range(W-1):
        if S[j] == 'T' and S[j+1] == 'T':
            S[j] = 'P'
            S[j+1] = 'C'
    print(''.join(S))