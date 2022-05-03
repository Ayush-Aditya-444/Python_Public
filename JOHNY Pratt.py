for _ in range(int(input())):
    n = int(input())
    lengths = list(map(int, input().split()))
    place = int(input())
    value = lengths[place-1]
    lengths.sort()
    for i in range(len(lengths)):
        if lengths[i] == value:
            print(i+1)
            break

