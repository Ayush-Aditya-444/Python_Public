# cook your dish here
for i in range(int(input())):
    a,b=map(int, input().split())
    if a<b:
        print("BIKE")
    elif a>b:
        print("CAR")
    else:
        print("SAME")