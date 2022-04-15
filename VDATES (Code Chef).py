for i in range(int(input())):
    a,b,c=map(int, input().split())
    if a>=b and a<=c:
        print("Take second dose now")
    elif a>b and a>c:
        print("Too Late")
    elif a<b and a<c:
        print("Too Early")