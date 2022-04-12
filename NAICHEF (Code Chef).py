for i in range(int(input())):
    a,b,c = map(int,input().split())
    list1=list(map(int,input().split()))
    d=list1.count(b)/a
    e=list1.count(c)/a
    print("{0:.10f}".format(d*e))