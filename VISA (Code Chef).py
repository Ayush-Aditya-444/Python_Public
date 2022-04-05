for i in range(int(input())):
    list1=list(map(int, input().split()))
    if list1[0]<=list1[1] and list1[2]<=list1[3] and list1[4]>=list1[5]:
        print("YES")
    else:
        print("NO")
