for _ in range(int(input())):
    a=int(input())
    b=set(map(int, input().split()))
    c=int(input())
    d=set(map(int, input().split()))
    print(b.issubset(d))