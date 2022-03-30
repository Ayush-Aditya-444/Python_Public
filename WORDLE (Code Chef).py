# cook your dish here
for i in range(int(input())):
    a=input()
    b=input()
    list1=[]
    for i in range(len(a)):
        if a[i]==b[i]:
            list1.append("G")
        else:
            list1.append("B")
    x = "".join(list1)
    print(x)