T = int(input())

result_list = []
for i in range(T):
    A,B,C = map(int,input().split())
    total = A + B + C
    result_list.append(min(A,C,total // 3))
    
for j in range(T):
    print(result_list[j])