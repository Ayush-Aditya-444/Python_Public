# cook your dish here
for i in range(int(input())):
    a,b,c=map(int, input().split())
    if (a+b)/2>=35 and (a+c)/2>=35 and (b+c)/2>=35:
        print("Pass")
    else:
        print("Fail")