a=int(input())
b=set()
b.update(list(map(int, input().split())))
c=int(input())
d=set()
d.update(list(map(int, input().split())))
e=b.difference(d)
print(len(e))