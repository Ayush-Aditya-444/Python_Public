# cook your dish here
for i in range(int(input())):
    a,b,c,d=list(map(int, input().split()))
    if a+c*d>b:
        print("overFlow")
    elif a+c*d==b:
        print("filled")
    else:
        print("Unfilled")