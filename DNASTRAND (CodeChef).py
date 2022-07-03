# cook your dish here
for i in range(int(input())):
    num1=int(input())
    str1=input()
    list1=[]
    for i in range(num1):
        if str1[i]=="A":
            list1.append("T")
        if str1[i]=="T":
            list1.append("A")
        if str1[i]=="C":
            list1.append("G")
        if str1[i]=="G":
            list1.append("C")
    print("".join(list1))