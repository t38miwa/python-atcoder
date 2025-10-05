n=int(input())

result=[]
for i in range(n):
    min_j=10
    for j in range(1,10):
        if n%j == 0:
            baisu=n//j
            if i%baisu==0:
                if j<min_j:
                    min_j=j
    if min_j!=10:
        result.append(str(min_j))
    else:
        result.append('-')

print(''.join(result))



#i=4のとき12/3は４、12/6は２で４はこれらの倍数になる
#i=3のとき12/4は3、12/は6で3はこれらの倍数になる