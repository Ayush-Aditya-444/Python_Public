for i in range(int(input())):
    list1=list(map(int, input().split()))
    a=list1[2]//list1[1]
    if list1[0]>a:
        print(a)
    else:
        print(list1[0])