for i in range(int(input())):
    customer,fruits,vegetables,fish=map(int,input().split())
    if vegetables<customer:
        print("NO")
    elif vegetables>=customer and fruits+fish>=customer:
        print("YES")
    else:
        print("NO")