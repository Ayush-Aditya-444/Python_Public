# cook your dish here
for i in range(int(input())):
    list1=list(map(int, input().split()))
    print(max(list1)-min(list1))