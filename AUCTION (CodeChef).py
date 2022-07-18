# cook your dish here
for i in range(int(input())):
    a,b,c=map(int, input().split())
    if c>b and c>a:
        print("Charlie")
    elif b>a and b>c:
        print("Bob")
    else:
        print("Alice")