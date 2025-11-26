def solution(N):
    binary = format(N,'b')
    
    max_gap = 0
    current_gap = 0
    started = False

    for bit in binary:
        print(bit)
        if bit == '1':
            if started:
                max_gap = max(max_gap,current_gap)
            started = True
            current_gap = 0
        else:
            if started:
                current_gap += 1
    return max_gap
            

N = int(input())
print(solution(N))