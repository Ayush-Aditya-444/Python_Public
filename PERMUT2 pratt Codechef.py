while True:
    a = int(input())
    if a == 0:
        break
    else:
        b = input().split()
    b = [int(i) for i in b]
    b.insert(0, 0)
    c = [0 for i in range(len(b) + 1)]
    for i in range(len(b)):
        c[b[i]] = i
    c.pop()
    if b == c:
        print("ambiguous")
    else:
        print("not ambiguous")

