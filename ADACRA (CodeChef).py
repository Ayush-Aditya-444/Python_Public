for _ in range(int(input())):
    s=input()
    l=list(s)
    a=0
    for i in range(len(s)-1):
        if l[i]!=l[i+1]:
            a=a+1
        else:
            continue
    if a%2==0:
        print(a//2)
    else:
        print(a//2+1)