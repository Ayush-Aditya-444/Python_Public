# cook your dish here
for _ in range(int(input())):
    a,b=map(int,input().split())
    if a%2!=0 and b%2!=0:
        print("NO")
    elif a==1 or b==1:
        print("NO")
    else:
        print("YES")