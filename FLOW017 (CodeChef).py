# cook your dish here
for i in range(int(input())):
    list1=list(map(int, input().split()))
    list1.sort()
    print(list1[-2])
    