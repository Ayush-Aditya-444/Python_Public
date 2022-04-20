for _ in range(int(input())):
    a=int(input())
    b=input()
    b=list(b)
    c=list("zyxwvutsrqponmlkjihgfedcba")
    d=list("abcdefghijklmnopqrstuvwxyz")
    e=-1
    list1=[]
    list2=[]
    for i in range(0, len(b)-1, 2):
        b[i], b[i+1] = b[i+1], b[i]
    for j in range(len(b)):
        for k in range(len(c)):
            if b[j]==c[k]:
                list1.append(k+1)
    for l in range(len(list1)):
        a=list1[l]
        list2.append(d[a-1])
    print("".join(list2))

