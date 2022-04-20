for i in range(int(input())):
    a,b,c,d,e=map(int, input().split())
    f=b-a
    if c*e<=f and d*e>=f:
        print(1)
    else:
        print(0)