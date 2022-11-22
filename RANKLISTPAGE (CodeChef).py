# cook your dish here
for i in range(int(input())):
    a=int(input())
    if a<25:
        print(1)
    elif a%25==0:
        print(a//25)
    else:
        print(a//25+1)