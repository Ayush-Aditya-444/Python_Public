# cook your dish here
for i in range(int(input())):
    a, b, c = map(int, input().split())
    for i in range(c):
        d,e = map(int, input().split())
        if b==d:
            b=e
        elif b==e:
            b=d
    print(b)