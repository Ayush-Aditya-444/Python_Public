for i in range(int(input())):
    a,b=map(int, input().split())
    list1=[]
    for i in range(a):
        c,d,e=map(int, input().split())
        if e<=b:
            list1.append(d*c)
    if len(list1)==0:
        print("no tablet")
    else:
        print(max(list1))
