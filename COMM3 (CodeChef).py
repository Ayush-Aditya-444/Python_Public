import math
for _ in range(int(input())):
    a=int(input())
    b,c=map(int, input().split())
    d,e=map(int, input().split())
    f,g=map(int, input().split())
    length1=math.sqrt( pow((e-c),2) + pow((d-b),2) )
    length2=math.sqrt( pow((g-e),2) + pow((f-d),2) )
    length3=math.sqrt( pow((c-g),2) + pow((b-f),2) )
    list1=[length1, length2, length3]
    list1.sort()
    if list1[1]<= a:
        print("yes")
    else:
        print('no')