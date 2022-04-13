for i in range(int(input())):
    a=int(input())
    list1=list(map(int, input().split()))
    list1.sort()
    print(sum(list1[1:]))