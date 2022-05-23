# cook your dish here
for i in range(int(input())):
    list1=list(map(int, input().split()))
    a=len(list1)
    list1.remove(a-1)
    list1.sort()
    print(list1[-1])