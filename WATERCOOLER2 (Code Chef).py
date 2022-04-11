import math
for i in range(int(input())):
    a,b=map(int, input().split())
    c=math.ceil(b/a) -1
    print(c)   