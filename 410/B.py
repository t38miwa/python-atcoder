N,Q = map(int,input().split())
X = list(map(int,input().split()))

# 箱4,ボール5
# どの箱にボールが何個入っているか管理する辞書
box = [0]*N

result = []
for i in range(Q):
    if X[i] >= 1:
        result.append(X[i])
        box[X[i]-1] += 1
    # ボールを、現在入っているボールが最も少ない箱のうち番号が最小である箱に入れる
    else:
        print(min(box))
        ind = box.index(min(box))
        # index = 0
        # min_box = box[0]
        # for j in range(N):
        #     if box[j] < min_box:
        #         min_box = box[j]
        #         index = j
        # box[index] += 1
        # result.append(index+1)
        box[ind] += 1
        result.append(ind+1)
print(*result)