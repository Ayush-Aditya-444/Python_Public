for i in range(int(input())):
    a,b=map(int, input().split())
    if a<=b and b%a==0:
        print("YES")
    else:
        print("NO")