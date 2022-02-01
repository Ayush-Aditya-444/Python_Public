z =[]
y = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    z+=[[name,score]]
    y+=[score]
b=sorted(list(set(y)))[1]
print(sorted(z))
print(y)
print(b)
for a,c in sorted(z):
    if c==b:
        print(a)