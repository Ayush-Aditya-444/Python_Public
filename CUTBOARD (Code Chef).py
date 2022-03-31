for i in range(int(input())):
    list1=list(map(int, input().split()))
    list2=list(map(int, input().split()))
    a=0
    b=0
    for i in range(list1[1]):
        if list2[i]==0:
            a=a+list1[2]
        else:
            b=b+list1[3]
    print(a+b)