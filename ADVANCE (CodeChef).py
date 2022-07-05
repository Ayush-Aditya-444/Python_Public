# cook your dish here
for i in range(int(input())):
    a,b=list(map(int, input().split()))
    if a<=b and a+200>=b:
        print("YES")
    else:
        print("NO")