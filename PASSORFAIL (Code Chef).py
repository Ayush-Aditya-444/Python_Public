# cook your dish here
for i in range(int(input())):
    list1=list(map(int, input().split()))
    a=list1[0]-list1[1]
    b=list1[1]*3
    c=b-a
    if c>=list1[2]:
        print("PASS")
    else:
        print("FAIL")