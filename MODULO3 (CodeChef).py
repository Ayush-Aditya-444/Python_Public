for i in range(int(input())):
    A, B = [int(i) for i in input().split()]
    if A % 3 ==0 or B % 3 == 0:
        print(0)
    elif A <= B:
        if (B-A) % 3 == 0:
            print(1)
        else:
            print(2)
    else:
        if (A-B) % 3 == 0:
            print(1)
        else:
            print(2)