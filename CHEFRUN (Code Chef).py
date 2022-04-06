# cook your dish here
for i in range(int(input())):
    list1=list(map(int, input().split()))
    a=abs(list1[2]-list1[0])
    b=abs(list1[2]-list1[1])
    c=a/list1[3]
    d=b/list1[4]
    if c<d:
        print("Chef")
    elif c>d:
        print("Kefa")
    else:
        print("Draw")