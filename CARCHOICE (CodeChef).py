for i in range(int(input())):
    list1=list(map(int, input().split()))
    a=list1[2]/list1[0]
    b=list1[3]/list1[1]
    if a>b:
        print(-1)
    elif a==b:
        print(0)
    else:
        print(1)