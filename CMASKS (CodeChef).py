for i in range(int(input())):
    a,b=map(int, input().split())
    if a*100>=b*10:
        print("Cloth")
    else:
        print("Disposable")