for i in range(int(input())):
    a,b=map(int, input().split())
    if a-b<0:
        print(abs(a-b))
    else:
        print(0)