for i in range(int(input())):
    a,b=map(int, input().split())
    c,d=map(int, input().split())
    e,f=map(int, input().split())
    print(max(a+b, c+d, e+f))
