# cook your dish here
for i in range(int(input())):
    a,b,c,d,e=map(int, input().split())
    list1=[a,b,c]
    list1.sort(reverse=True)
    print(list1)
    if sum(list1)<=d:
        print("Yes")
    elif list1[0]+list1[1]<=d and list1[2]<=e:
        print("Yes")
    else:
        print("No")