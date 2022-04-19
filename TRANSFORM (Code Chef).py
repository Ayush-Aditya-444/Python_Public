for i in range(int(input())):
    a=int(input())
    if a%3==2:
        print("SMALL")
    elif a%3==1:
        print("HUGE")
    else:
        print("NORMAL")