from traceback import print_tb


for i in range(int(input())):
    list1=list(map(int, input().split()))
    if list1[0]<=list1[4] and list1[1]<=list1[5] and list1[2]<=list1[6]:
        if list1[4]+list1[5]+list1[6]>=list1[3]:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")