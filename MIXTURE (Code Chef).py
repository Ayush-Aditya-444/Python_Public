for i in range(int(input())):
    a,b=map(int, input().split())
    if a==0 and b>0:
        print("Liquid")
    elif a>0 and b==0:
        print("Solid")
    else:
        print("Solution")