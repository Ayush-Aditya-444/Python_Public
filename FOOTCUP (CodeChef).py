for i in range(int(input())):
    a,b=map(int, input().split())
    if a==b and a>0 and b>0:
        print("YES")
    else:
        print("NO")