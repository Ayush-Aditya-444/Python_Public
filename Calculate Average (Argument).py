list1=list(map(int, input().split()))
def avg(*a):
    b=0
    for i in range (len(a)):
        b+=a[i]
    return b
print(avg(*list1)/len(list1))