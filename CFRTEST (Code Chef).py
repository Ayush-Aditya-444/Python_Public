for i in range(int(input())):
    a=int(input())
    list1=list(map(int, input().split()))
    list2=[]
    for i in list1:
        if i not in list2:
            list2.append(i)
    print(len(list2))

