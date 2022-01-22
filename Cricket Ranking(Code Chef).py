print("Enter No. Of Test Cases:-")
for i in range(int(input())):
    list1=input().split()
    list2=input().split()
    if int(list1[0])>int(list2[0]) and int(list1[1])>int(list2[1]) and int(list1[2])<int(list2[2]):
        print("A")
    elif int(list1[0])>int(list2[0]) and int(list1[1])<int(list2[1]) and int(list1[2])>int(list2[2]):
        print("A")
    elif int(list1[0])<int(list2[0]) and int(list1[1])>int(list2[1]) and int(list1[2])>int(list2[2]):
        print("A")
    elif int(list1[0])>int(list2[0]) and int(list1[1])>int(list2[1]) and int(list1[2])>int(list2[2]):
        print("A")
    else:
        print("B")