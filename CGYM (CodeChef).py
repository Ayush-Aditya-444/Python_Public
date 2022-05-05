# cook your dish here
for i in range(int(input())):
    a,b,c=map(int, input().split())
    if a<=c:
        if a+b<=c:
            print(2)
        else:
            print(1)
    else:
        print(0)