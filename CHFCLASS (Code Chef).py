for i in range(int(input())):
    a=int(input())
    b=a//7
    c=a%7
    if c>=6:
        print(b+1)
    else:
        print(b)