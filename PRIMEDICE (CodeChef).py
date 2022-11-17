# cook your dish here
for i in range(int(input())):
    a,b=map(int, input().split())
    c=a+b
    p=0
    for j in range(2,c):
        if c%j==0:
            print("Bob")
            p=1
            break
    if p==0:
        print("Alice")
        
        