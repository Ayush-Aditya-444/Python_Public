#Method 1 (Iterative)
def ayush1(list1,int1):
    list1.sort()
    list1=list(set(list1))
    return list1[-int1],list1[int1-1]


list1=list(map(int, input().split()))
int1=int(input())
print(ayush1(list1,int1))
