# cook your dish here
# cook your dish here
for i in range(int(input())):
    a,b,c=map(int, input().split())
    if (a+b)%2!=0:
        print("YES")
    elif (a+c)%2!=0:
        print("YES")
    elif (b+c)%2!=0:
        print("YES")
    else:
        print("NO")