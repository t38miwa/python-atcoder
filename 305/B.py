P,Q = input().split()
num_P = ord(P) - 65
num_Q = ord(Q) - 65

dis = [3,1,4,1,5,9]

S = [0]*7

for i in range(6):
    S[i+1] = S[i] + dis[i]

print(abs(S[num_P] - S[num_Q]))