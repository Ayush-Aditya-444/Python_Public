for i in range(int(input())):
    list1=list(map(int, input().split()))
    a=list1[0]-list1[1]
    if a<0:
        print(0)
    else:
        print(a*list1[2])