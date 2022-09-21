# cook your dish here
for _ in range(int(input())):
    a,b,c,d=map(int, input().split())
    if a/b<c/d:
        print("Bob")
    elif a/b>c/d:
        print("Alice")
    else:
        print("Equal")