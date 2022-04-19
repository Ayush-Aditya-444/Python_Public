for i in range(int(input())):
    a,b,c=map(int, input().split())
    if a<=b*c:
        print("Yes")
    else:
        print("No")
