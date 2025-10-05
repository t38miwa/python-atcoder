h,w=map(int,input().split())

a=[input() for i in range(h)]
b=[input() for i in range(h)]


for i in range(h):
    for j in range(w):
        a[i][j]=a[i+1][j]
        
def shift_y():
for i in range(h):
    for j in range(w):
        a[i][j]=a[i][j+1]