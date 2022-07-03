for _ in range(int(input())):
    a=int(input())
    list1=list(map(int, input().split()))
    max1=0
    for i in range(len(list1)):
        if list1.count(list1[i])>max1:
            max1=list1.count(list1[i])
    print(len(list1)-max1)