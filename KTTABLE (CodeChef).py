for i in range(int(input())):
    a=int(input())
    list1=list(map(int, input().split()))
    list2=list(map(int, input().split()))
    count1=0
    list1.append(0)
    list1.sort()
    for i in range(len(list1)-1):
        if list1[i+1]-list1[i]>=list2[i]:
            count1+=1
        else:
            continue
    print(count1)
    