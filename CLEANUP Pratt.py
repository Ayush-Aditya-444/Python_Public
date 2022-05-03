for _ in range(int(input())):
    n, m = map(int, input().split())
    finish = list(map(int, input().split()))
    not_finish = []
    for j in range(1, n + 1):
        if j not in finish:
            not_finish.append(j)
    not_finish.sort()
    chef = []
    other = []
    for j in range(len(not_finish)):
        if j % 2 == 0:
            chef.append(not_finish[j])
        else:
            other.append(not_finish[j])
    for j in chef:
        print(j, end=' ')
    print()
    for j in other:
        print(j, end=' ')
    print()
