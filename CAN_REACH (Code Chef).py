for i in range(int(input())):
    list1=list(map(int, input().split()))
    if list1[0]%list1[2]==0 and list1[1]%list1[2]==0:
        print("YES")
    else:
        print("NO")