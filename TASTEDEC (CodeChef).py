# cook your dish here
for i in range(int(input())):
    a,b=map(int, input().split())
    int1=2*a
    int2=5*b
    if int1==int2:
        print("Either")
    elif int1>int2:
        print("Chocolate")
    else:
        print("Candy")