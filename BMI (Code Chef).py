for i in range(int(input())):
    a,b=map(int, input().split())
    c=a/pow(b,2)
    if c<=18:
        print(1)
    elif c in range(19,25):
        print(2)
    elif c in range(25,30):
        print(3)
    else:
        print(4)
