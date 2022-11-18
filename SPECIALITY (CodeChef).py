# cook your dish here
for i in range(int(input())):
    list1=list(map(int, input().split()))
    int1=max(list1)
    if list1[0]==int1:
        print("Setter")
    elif list1[1]==int1:
        print("Tester")
    else:
        print("Editorialist")