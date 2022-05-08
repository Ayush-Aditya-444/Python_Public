for i in range(int(input())):
    a,b,c=map(int, input().split())
    if a>=b:
        print("PIZZA")
    elif a>=c:
        print("BURGER")
    else:
        print("NOTHING")