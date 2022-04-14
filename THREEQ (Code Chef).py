for i in range(int(input())):
    list1=list(map(int, input().split()))
    list2=list(map(int, input().split()))
    list1.sort()
    list2.sort()
    a=0
    for i in range(len(list1)):
        if list1[i]==list2[i]:
            a=a+1
    if a==len(list1):
        print("Pass")
    else:
        print("Fail")

