for i in range(int(input())):
    a,b=map(int, input().split())
    if (b-a-1)%3==0 or (b-a)%3==0:
        print("YES")
    else:
        print("NO")