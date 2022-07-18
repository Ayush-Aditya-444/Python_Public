import math
for i in range(int(input())):
    a,b=map(int, input().split())
    if a-b>0:
        print((math.ceil((b-a)//4))*(-1))
    else:
        print(0)