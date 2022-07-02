# cook your dish here
for i in range(int(input())):
    a,b,c=map(int, input().split())
    if a<=c and b>c:
        print("YES")
    else:
        print("NO")