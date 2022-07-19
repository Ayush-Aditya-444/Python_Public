# cook your dish here
for i in range(int(input())):
    a,b,c,d=map(int, input().split())
    if a+b>=c+d:
        print(c+d)
    else:
        print(a+b)