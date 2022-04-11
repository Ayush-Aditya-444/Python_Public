for i in range(int(input())):
    a,b=map(int, input().split())
    if a>b:
        print("SECOND")
    elif a==b:
        print("ANY")
    else:
        print("FIRST")