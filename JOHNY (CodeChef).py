for i in range(int(input())):
    length_list1=int(input())
    list1=list(map(int, input().split()))
    uncle_johny=int(input())
    num1=list1[uncle_johny-1]
    list1.sort()
    print(list1.index(num1)+1)