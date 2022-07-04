# cook your dish here
for i in range(int(input())):
    a,b,c=list(map(int, input().split()))
    if a+b<c:
        print("YES")
    elif b+c<a:
        print("YES")
    elif a+c<b:
        print("YES")
    else:
        print("NO")