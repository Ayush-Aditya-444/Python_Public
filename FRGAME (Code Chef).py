for i in range(int(input())):
    a,b,c,d=map(int, input().split())
    if a>=b:
        b+=c
    else:
        a+=c
    if a>=b:
        b+=d
    else:
        a+=d
    if a>=b:
        print("N")
    else:
        print("S")
