# cook your dish here
for _ in range(int(input())):
    a,b=map(int,input().split())
    if a-b>b:
        print(b)
    else:
        print(a-b)