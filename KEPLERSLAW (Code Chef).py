# cook your dish here
import math
for i in range(int(input())):
    a,b,c,d=map(int, input().split())
    e=pow(a,2)/pow(c,3)
    f=pow(b,2)/pow(d,3)
    if e==f:
        print("Yes")
    else:
        print("No")