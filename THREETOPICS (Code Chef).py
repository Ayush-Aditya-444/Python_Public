for i in range(int(input())):
    list1=list(map(int, input().split()))
    a=0
    for i in range(len(list1)-1):
        if list1[3]==list1[i]:
            a+=1
    if a>0:
        print("YES")
    else:
        print("NO")
