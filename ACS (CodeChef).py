# cook your dish here
for i in range(int(input())):
    a=int(input())
    num1=a//100+a%100
    if num1>10:
        print(-1)
    else:
        print(num1)