for i in range(int(input())):
    int1=int(input())
    list1=[]
    for i in range(int1):
        a=int(input())
        if a not in list1:
            list1.append(a)
        else:
            list1.remove(a)
    print(*list1)