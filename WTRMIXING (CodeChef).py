# cook your dish here
for i in range(int(input())):
    a,b,c,d=map(int, input().split())
    if a>b:
        if a-b<=d:
            print("YES")
        else:
            print("NO")
    else:
        if b-a<=c:
            print("YES")
        else:
            print("NO")