for i in range(int(input())):
    list1=list(map(int, input().split()))
    a=list1[0]*list1[1]
    b=list1[0]+list1[2]
    print(min(a,b))