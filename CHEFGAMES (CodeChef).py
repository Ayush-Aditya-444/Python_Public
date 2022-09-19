# cook your dish here
for _ in range(int(input())):
    list1=list(map(int,input().split()))
    if len(set(list1))==1 and list1[0]==0:
        print("IN")
    else:
        print("OUT")