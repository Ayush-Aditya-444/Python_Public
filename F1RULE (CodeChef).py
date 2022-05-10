# cook your dish here
for i in range(int(input())):
    a,b=map(int, input().split())
    if a*1.07>=b:
        print("YES")
    else:
        print("NO")