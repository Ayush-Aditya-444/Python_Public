for i in range(int(input())):
    list1=list(map(int, input().split()))
    print(max(abs(list1[0]-list1[2]), abs(list1[1]-list1[3])))