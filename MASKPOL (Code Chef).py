for i in range(int(input())):
    a,b=map(int, input().split())
    c=a-b
    print(min(c,b))