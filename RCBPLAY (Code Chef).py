for i in range(int(input())):
    list1=list(map(int, input().split()))
    a=list1[1]-list1[0]
    b=list1[2]*2
    if a>b:
        print("NO")
    else:
        print("YES")