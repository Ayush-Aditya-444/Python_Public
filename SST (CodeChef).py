for i in range(int(input())):
    a,b=map(int, input().split())
    if a*10==b*5:
        print("ANY")
    elif a*10>b*5:
        print("FIRST")
    else:
        print("SECOND")