# cook your dish here
for i in range(int(input())):
    a,b,c,d=map(int, input().split())
    sum1=a+c*10
    sum2=b+d*10
    if sum1==sum2:
        print("Draw")
    elif sum1>sum2:
        print("Chefina")
    else:
        print("Chef")