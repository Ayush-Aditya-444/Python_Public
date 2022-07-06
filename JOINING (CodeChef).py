import math
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    a=math.ceil(n/5)
    b=math.ceil(k/5)
    s=a-b
    print(s)