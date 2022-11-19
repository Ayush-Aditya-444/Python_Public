# cook your dish here
for i in range(int(input())):
    a,b,c=map(int, input().split())
    int1=(a+b)/2
    if int1>c:
        print("YES")
    else:
        print("NO")