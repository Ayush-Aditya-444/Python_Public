list1=list(map(int, input().split()))
def max_function(*a):
    b=a[0]
    for i in range(len(a)-1):
        if (b<a[i+1]):
            b=a[i+1]
            pass
        else:
            pass
    return b
print(max_function(*list1))