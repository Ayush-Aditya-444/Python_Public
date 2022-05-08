for i in range(int(input())):
    a=int(input())
    b=input()
    c=d=0
    while c<len(b):
        if c<len(b)-1 and b[c]==b[c+1]:
            d+=1
            c+=2
        else:
            d+=1
            c+=1
    print(d)