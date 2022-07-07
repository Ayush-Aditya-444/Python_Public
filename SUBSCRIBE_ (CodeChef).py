for i in range(int(input())):
    a,b=map(int, input().split())
    if a%6==0:
        print(b*(a//6))
    else:
        print(b*((a//6)+1))