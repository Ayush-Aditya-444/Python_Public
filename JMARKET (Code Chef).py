for i in range(int(input())):
    x,a,b,c = map(int,input().split())
    k = [a,b,c]
    k.sort()
    print((x-1)*k[0] + k[1])