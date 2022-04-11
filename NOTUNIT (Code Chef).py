# cook your dish here
from math import gcd


for i in range(int(input())):
    list1=[]
    a,b=map(int, input().split())
    for j in range(a,b-1):
        for k in range(a+1,b):
            if gcd(j,k)>1:
                list1.append(j)
                list1.append(k)
    if len(list1)==0:
        print(-1)
    else:
        print(list1[0],list1[1])