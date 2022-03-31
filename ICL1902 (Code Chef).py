import math
for i in range(int(input())):
    a=int(input())
    b=0
    while a>0:
        c=math.floor(math.sqrt(a))
        a-=(c*c)
        b+=1
    print(b)