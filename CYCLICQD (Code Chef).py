for i in range(int(input())):
    list1=list(map(int, input().split()))
    if list1[0]+list1[2]==180 and list1[1]+list1[3]==180:
        print("YES")
    else:
        print("NO")