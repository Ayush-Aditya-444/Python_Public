for i in range(int(input())):
    list1=list(map(int, input().split()))
    a=sum(list1[0:5])*list1[-1]
    if a <= 120:
        print('No')
    else:
        print('Yes')