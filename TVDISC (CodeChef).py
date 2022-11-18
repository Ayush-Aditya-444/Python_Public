# cook your dish here
for i in range(int(input())):
    list1=list(map(int, input().split()))
    int1=list1[0]-list1[2]
    int2=list1[1]-list1[3]
    if int1==int2:
        print("Any")
    elif int1>int2:
        print("Second")
    else:
        print("First")