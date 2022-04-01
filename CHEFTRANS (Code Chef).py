for i in range(int(input())):
    a,b,c = map(int,input().split())
    if a+b<c:
        print("PLANEBUS")
    elif a+b==c:
        print("EQUAL")
    else:
        print("TRAIN")