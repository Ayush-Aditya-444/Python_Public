for i in range(int(input())):
    list1=list(map(int, input().split()))
    a=(list1[1]+((100-list1[0])*list1[2]))*10
    print(a)