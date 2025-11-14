# 高橋くん頭パーツ6個、体パーツ6個持ってる
# ２番目の頭パーツは7,２番目の体パーツは8
# 倒れないロボットを合計3体作りたい
# 二重for文回した時点でTLE

# H<Bとなるような組み合わせをK個作りたい
# Hの3つ目が2,つまり、Bに2以上の値が3以上あればYes
N,M,K = map(int,input().split())
H = list(map(int,input().split()))
B = list(map(int,input().split()))

sh = sorted(H)
sb = sorted(B)

cnt = 0

indH = 0

