for i in range(int(input())):
    p,q=map(int,input().split())
    if((p+q)//2%2==0):
        print("Alice")
    else:
        print("Bob")