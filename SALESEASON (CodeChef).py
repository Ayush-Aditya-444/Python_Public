# cook your dish here
for i in range(int(input())):
    a=int(input())
    if a>100 and a<=1000:
        print(a-25)
    elif a>1000 and a<=5000:
        print(a-100)
    elif a>5000:
        print(a-500)
    else:
        print(a)