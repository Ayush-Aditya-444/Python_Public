for i in range(int(input())):
    list1=list(map(int, input().split()))
    list2=list(map(int, input().split()))
    a=0
    for i in range(len(list2)):
        if list1[1]<list2[i]:
            a=a+1
    print(a)