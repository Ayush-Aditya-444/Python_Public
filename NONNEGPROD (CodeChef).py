# cook your dish here
for _ in range(int(input())):
    a=int(input())
    list1=list(map(int, input().split()))
    count1=1
    for i in range(len(list1)):
        count1*=list1[i]
    if count1>=0:
        print(0)
    else:
        print(1)