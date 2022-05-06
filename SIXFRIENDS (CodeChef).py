for i in range(int(input())):
    a,b=map(int, input().split())
    if a*3>b*2:
        print(b*2)
    else:
        print(a*3)