# cook your dish here
for _ in range(int(input())):
    n=int(input())
    s=input()
    l=[]
    i=0
    while i<n:
        if s[i]=="0":
            if s[i+1]=="0":
                l.append("A")
            else:
                l.append("T")
        else:
            if s[i+1]=="0":
                l.append("C")
            else:
                l.append("G")
        i=i+2
    s=[str(i) for i in l]
    st="".join(s)
    print(st)