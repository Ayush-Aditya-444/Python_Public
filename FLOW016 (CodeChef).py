# cook your dish here
T = int(input())
for i in range(T):
    num = [int(x) for x in input().split(' ')]
    a = min(num)
    b = max(num)
    multiply = a*b
    while(b):
        a,b = b,a%b
    hcf = a
    lcm = multiply/hcf
    print(hcf,int(lcm))