# cook your dish here
for _ in range(int(input())):
    int1=int(input())
    list1=list(map(int, input().split()))
    set1=list(set(list1))
    count1=1
    for i in range(len(set1)):
        if set1[i]+1 not in list1:
            count1+=1
            if count1==3:
                print("NO")
                break
    if count1!=3:
        print("YES")
    