for i in range(int(input())):
    list1=list(map(int, input().split()))
    a=list1[0]-list1[1]
    b=list1[2]+list1[3]+list1[4]
    if a>=b:
        print("YES")
    else:
        print("NO")