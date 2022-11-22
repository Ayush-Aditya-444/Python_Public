# cook your dish here
for i in range(int(input())):
    a,b=map(int, input().split())
    if (b/a)*100>=50:
        print("YES")
    else:
        print("NO")