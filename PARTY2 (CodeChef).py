# cook your dish here
for i in range(int(input())):
    a,b,c=list(map(int, input().split()))
    if a*b<=c:
        print("YES")
    else:
        print("NO")