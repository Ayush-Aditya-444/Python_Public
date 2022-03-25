for i in range(int(input())):
    a=int(input())
    b=0
    list1=list(map(int, input().split()))
    list2=list(map(int, input().split()))
    for i in range(len(list1)):
        if list1[i]==list2[i]:
            b=b+1
    print(b)