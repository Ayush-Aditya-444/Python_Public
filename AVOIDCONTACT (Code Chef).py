for _ in range(int(input())):
    x,y = map(int,input().split())
    if x>0 and y==0:
        print(x)
    elif x>0 and x==y:
        print(x+y-1)
    elif x>0 and x>y:
        print(x+y)