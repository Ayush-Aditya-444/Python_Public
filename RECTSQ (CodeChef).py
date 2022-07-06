# cook your dish here
import math
t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    a=math.gcd(n,m)
    print((n//a)*(m//a))