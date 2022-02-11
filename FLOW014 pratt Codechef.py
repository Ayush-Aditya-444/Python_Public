for _ in range(int(input())):
    hard, carbon, tens = map(float, input().split())
    a, b, c = hard > 50, carbon < 0.7, tens > 5600
    if a and b and c:
        print(10)
    elif a and b and not c:
        print(9)
    elif b and c and not a:
        print(8)
    elif a and c and not b:
        print(7)
    elif a or b or c:
        print(6)
    else:
        print(5)
