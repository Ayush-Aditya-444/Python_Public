for i in range(int(input())):
    list1=list(map(int, input().split()))
    a=2
    for j in range(0,2):
        for k in range(2,4):
            if list1[j]==list1[k]:
                a=a-1
    print(a)
