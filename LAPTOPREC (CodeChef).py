n=int(input())
for _ in range(n):
    x=int(input())
    list1= [int(i) for i in input().split()][:x]
    res=[0 for i in range(10)]
    
    for i in range(10):
        res[i]=list1.count(i+1)
    
    m = max(res)
    if (res.count(m)>1):
        print("confused")
    else:
        print(res.index(m)+1)