import math

x= [0]*3
y= [0]*3

for i in range(3):
    x[i],y[i]=map(int,input().split())

a=math.sqrt((x[2]-x[0])**2+(y[2]-y[0])**2)
b=math.sqrt((x[1]-x[0])**2+(y[1]-y[0])**2)
c=math.sqrt((x[2]-x[1])**2+(y[2]-y[1])**2)

result=False
if a**2+b**2==c**2:
    result=True
elif a**2+c**2==b**2:
    result=True
elif c**2+b**2==a**2:
    result=True

print("Yes" if result else "No")