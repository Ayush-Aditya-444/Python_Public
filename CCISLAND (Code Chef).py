for i in range(int(input())):
    list1=list(map(int, input().split()))
    a=min(list1[0]/list1[2], list1[1]/list1[3])
    if a>=list1[4]:
        print("YES")
    else:
        print("NO")