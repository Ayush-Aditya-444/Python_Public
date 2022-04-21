# cook your dish here
import math
for i in range(int(input())):
    list1=list(map(int, input().split()))
    list1.pop(0)
    list2=[]
    a=(math.gcd(*list1))
    for j in list1:
        b=j//a
        list2.append(b)
    print(*list2)