print("Enter No. Of Test Cases:-")
for i in range(int(input())):
    list1=input().split()
    b=int(list1[0])
    c=int(list1[1])
    d=int(list1[2])
    if b<c and b<d:
        print("Draw")
    elif c<b and c<d:
        print("Bob")
    elif d<b and d<c:
        print("Alice")