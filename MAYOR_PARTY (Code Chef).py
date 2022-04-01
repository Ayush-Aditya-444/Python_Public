for i in range(int(input())):
    list1=list(map(int, input().split()))
    if list1[1]>=list1[0]+list1[2]:
        print(list1[1])
    else:
        print(list1[0]+list1[2])