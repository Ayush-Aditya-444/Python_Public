# cook your dish here
for _ in range(int(input())):
    int1=int(input())
    list1=[]
    for i in range(int1):
        str1=input()
        list2=[]
        for j in range(len(str1)):
            if str1[i]=="1":
                list2.append(i)
        list1.append(list2[:])
    set1=set(list1[0])
    set2=set(list1[1])
    set3=set1.intersection(set2)
    for i in range(2,len(list1)):
        set4=list1[i]
        set3=set3.intersection(set4)
    print(len(set3))