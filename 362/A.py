R,G,B=map(int,input().split())
C=input()

if C=='Blue':
    if R>G:
        print(G)
    else:
        print(R)
if C=='Green':
    if R>B:
        print(B)
    else:
        print(R)
if C=='Red':
    if B>G:
        print(G)
    else:
        print(B)
