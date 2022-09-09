for i in range(int(input())):
    c=0
    x=int(input())
    y=list(input())
    if(len(y)==1):
        print("1")
    else:
        for i in range(0,len(y)-1):
            if(y[i]>y[i+1]):
                c=c+1 