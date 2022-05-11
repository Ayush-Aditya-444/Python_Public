for i in range(int(input())):
    a,b=map(int, input().split())
    list1=list(map(int, input().split()))
    list1.sort()
    print(list1[((a+b+1)//2)-1])