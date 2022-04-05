for i in range(int(input())):
    list1=list(map(int, input().split()))
    a=0
    b=0
    for i in range(len(list1)):
        if list1[i]==0:
            a=a+1
    else:
        b=b+1
    if a<b:
        print("NO")
    else:
        print("YES")