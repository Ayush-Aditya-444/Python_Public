for i in range(int(input())):
    list1=list(map(int, input().split()))
    list2=[]
    for i in range(list1[0]):
        a,b=map(int, input().split())
        if list1[1]>=a:
            list2.append(b)
    print(max(list2))
    list2.clear()

