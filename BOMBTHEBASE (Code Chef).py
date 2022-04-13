for i in range(int(input())):
    n,x = map(int,input().split())
    a=list(map(int,input().split()))
    c=0
    b=0
    for i in a:
        c+=1
        if i<x:
            b=c
    print(b)