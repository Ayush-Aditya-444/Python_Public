for i in range(int(input())):
    a,b=map(int, input().split())
    if a%b==0:
        print(a//b)
    elif a==0:
        print(0)
    else:
        print(-1)