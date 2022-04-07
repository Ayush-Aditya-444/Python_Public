for i in range(int(input())):
    a=int(input())
    b=input()
    c=0
    d=0
    for i in range(len(b)):
        if b[i]=="C":
            c=c+2
        elif b[i]=="D":
            c=c+1
            d=d+1
        else:
            d=d+2
    if c==d:
        print(55*a)
    elif c>d:
        print(60*a)
    else:
        print(40*a)