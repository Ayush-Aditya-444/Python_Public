for i in range(int(input())):
    list1=list(map(int, input().split()))
    if min(list1)==list1[0]:
        print("Draw")
    elif min(list1)==list1[1]:
        print("Bob")
    elif min(list1)==list1[2]:
        print("Alice")