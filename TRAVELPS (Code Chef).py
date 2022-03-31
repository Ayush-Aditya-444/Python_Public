for i in range(int(input())):
    list1=list(map(int, input().split()))
    b=input()
    c=0
    d=0
    for i in range(len(b)):
        if b[i]=="0":
            c=c+1
        if b[i]=="1":
            d=d+1
    e=(list1[1]*c)+(list1[2]*d)
    print(e)