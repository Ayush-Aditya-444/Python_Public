for i in range(int(input())):
    list1=list(map(int, input().split()))
    a=list1[0]
    b=a//3
    list1[0]=list1[0]-b
    print(list1[1]*list1[0])