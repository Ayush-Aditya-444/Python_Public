for i in range(int(input())):
    list1=list(map(int, input().split()))
    a=abs(list1[0]-list1[1])
    if a<=list1[2]:
        print("YES")
    else:
        print("NO")