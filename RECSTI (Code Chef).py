from itertools import count


for i in range(int(input())):
    a=int(input())
    list1=list(map(int, input().split()))
    a=0
    if len(list1)<=4:
        print(4-len(list1))
    else:
        for j in range(len(list1)):
            b=list1.count(list1[j])
            if b%2!=0:
                a=a+1
                list1.append(list1[j])
            else:
                continue
        print(a)

