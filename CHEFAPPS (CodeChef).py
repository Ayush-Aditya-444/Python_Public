# cook your dish here
for i in range(int(input())):
    a,b,c,d=map(int, input().split())
    if a>=b+c+d:
        print(0)
    else:
        if b+d<=a:
            print(1)
        else:
            print(2)