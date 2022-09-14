def ayush(list1):
    list1.sort()
    product1=list1[-3]*list1[-2]*list1[-1]
    product2=list1[0]*list1[1]*list1[-1]
    if product1>product2:
        return product1
    else:
        return product2

list1=[-5,-2,-1,0,7,1,1,5]
print(ayush(list1))