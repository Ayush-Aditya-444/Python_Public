for i in range(int(input())):
    a,b,c,d,e,f=map(int, input().split())
    if a==c or a==d:
        if b==c or b==d:
            print(1)
        else:
            print(0)
    elif a==e or a==f:
        if b==e or b==f:
            print(2)
        else:
            print(0)
    else:
        print(0)