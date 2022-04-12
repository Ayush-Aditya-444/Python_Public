for i in range(int(input())):
    a=int(input())
    list1=list(map(int, input().split()))
    list2=list(map(int, input().split()))
    list1.sort()
    list2.sort()
    if sum(list1[:(a-1)])==sum(list2[:(a-1)]):
        print("Draw")
    elif sum(list1[:(a-1)])>sum(list2[:(a-1)]):
        print("Alice")
    else:
        print("Bob")
