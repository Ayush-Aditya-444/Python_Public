for i in range(int(input())):
    a=int(input())
    b=input()
    c=0
    d=0
    list1=[]
    e=""
    for i in range(len(b)):
        if b[i]=="0":
            c=c+1
        if b[i]=="1":
            d=d+1
    for i in range(c):
        list1.append("0")
    for i in range(d):
        list1.append("1")
    e=e.join(list1)
    print(e)
