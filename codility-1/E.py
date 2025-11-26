# カエルは最初位置0
# 位置X+1に行きたい
# 時刻2に位置1に葉が落ちる
# カエルが川を渡れる最も早い時刻は？
# 全ての位置に葉があるときのみ川を渡れる

def solution(A,X):
    place_lst = []
    ans_int = "".join(map(str, range(1, X+1)))
    print(ans_int)
    for i in range(len(A)):
        if str(A[i]) not in place_lst:
            place_lst.append(str(A[i]))
            place_lst.sort()
            print(''.join(place_lst))
            if ''.join(place_lst) == ans_int:
                return i

A = list(map(int,input().split()))
X = int(input())

print(solution(A,X))