for i in range(int(input())):
    list1=list(map(int, input().split()))
    if list1[0]*list1[1]<=list1[2]*list1[3]:
        print("Yes")
    else:
        print("No")