for _ in range(int(input())):
    list1=list(map(int,input().strip().split()))
    a = input()
    b=0
    d="abcdefghijklmnopqrstuvwxyz"
    for i in range(len(list1)):
        if d[i] not in a:
            b=b+list1[i]
    print(b)