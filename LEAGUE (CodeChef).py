import math
for _ in range(int(input())):
    n = int(input())
    if n==2:
        print(3)
    elif n==3:
        print(3)
    else:
        a = 3*(n-1)
        b = int(3*math.ceil((n-2)/2))
        print(a-b)