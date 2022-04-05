# cook your dish here
# cook your dish here
import math
for i in range(int(input())):
    a,b=map(int,input().split())
    e=math.sqrt(b*b+a*a)
    d=math.sqrt(b*b-a*a)
    print(d,e)