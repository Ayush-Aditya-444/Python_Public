for i in range(int(input())):
    a,b,c,d=map(int, input().split())
    e=a+((a*d)//100)
    if e>=b and e<=c:
        print("Yes")
    else:
        print("No")