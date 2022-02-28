n = int(input())
s = set(map(int,input().split()))
for i in range(int(input())):
    ip = input().split()
    if ip[0]=="intersection_update":
        lp = set(map(int, input().split()))
        s.intersection_update(lp)
    elif ip[0]=="symmetric_difference_update":
        lp = set(map(int, input().split()))
        s.symmetric_difference_update(lp)
    elif ip[0]=="difference_update":
        lp = set(map(int, input().split()))
        s.difference_update(lp)
    elif ip[0]=="update":
        lp = set(map(int, input().split()))
        s.update(lp)
print(sum(list(s)))