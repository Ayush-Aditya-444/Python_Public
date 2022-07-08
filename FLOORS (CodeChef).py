import math
for i in range(int(input())):
    x,y=map(int,input().split())
    x1=math.ceil(x/10)
    y1=math.ceil(y/10)
    print(abs(x1-y1))