import math
for i in range(int(input())):
    a,b=map(int, input().split())
    list1=list(map(int, input().split()))
    c=0
    for i in range(len(list1)):
        c+=math.ceil(list1[i]/b)
    if max(list1)>c:
        print(c)
    else:
        print(max(list1))