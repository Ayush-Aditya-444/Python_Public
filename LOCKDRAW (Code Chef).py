for i in range(int(input())):
    list1=list(map(int, input().split()))
    list1.sort()
    if list1[0]+list1[1]==list1[2]:
        print("YES")
    else:
        print("NO")