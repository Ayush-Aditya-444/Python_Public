import math
for i in range(int(input())):
    a,b=map(int, input().split())
    print(math.ceil((b-a)/8))