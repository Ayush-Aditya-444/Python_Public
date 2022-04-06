for i in range(int(input())):
    a=int(input())
    list1=list(map(int, input().split()))
    for i in range(1,32):
        if i%7==0 or i%7==6:
            list1.append(i)
    res = []
    [res.append(x) for x in list1 if x not in res]
    print(len(res))
