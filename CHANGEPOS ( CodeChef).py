# cook your dish here
T = int(input())

for i in range(T):
    sx, sy, ex, ey = map(int, input().split())
    if sx != ex and sy != ey:
        print(1)
    else:
        print(2)