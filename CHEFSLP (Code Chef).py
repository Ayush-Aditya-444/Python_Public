for i in range(int(input())):
    list1=list(map(int, input().split()))
    if (list1[0]/2)>=list1[1]:
        print(list1[1]*list1[2])
    elif (list1[0]/2)<=list1[1]:
        a=list1[0]-list1[1]
        print(a*list1[2])
