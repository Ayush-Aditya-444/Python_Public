for i in range(int(input())):
    a=int(input())
    list1=list(map(int, input().split()))
    b=set(list1)
    list2=[]
    for j in b:
        c=list1.count(j)
        list2.append(c)
    print(a-max(list2))