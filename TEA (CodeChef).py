for i in range(int(input())):
    a,b,c=map(int, input().split())
    if a%b!=0:
        d=(a//b)+1
    else:
        d=a//b
    print(c*d)