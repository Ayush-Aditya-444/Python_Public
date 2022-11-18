# cook your dish here
for i in range(int(input())):
    a,b=map(int, input().split())
    if a==b:
        print("ANY")
    elif a>b:
        print("NEW PHONE")
    else:
        print("REPAIR")