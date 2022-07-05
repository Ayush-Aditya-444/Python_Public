# cook your dish here
for i in range(int(input())):
    a,b=list(map(int, input().split()))
    if 7-a>=7-b:
        print(7-b)
    else:
        print(7-a)