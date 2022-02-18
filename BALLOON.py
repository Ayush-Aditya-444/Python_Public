for _ in range(int(input())):
    new = [1, 2, 3, 4, 5, 6, 7]
    total = int(input())
    prob = list(map(int, input().split()))
    if total <= 7:
        print(total)
    else:
        maxi = 0
        for i in range(len(prob)):
            if prob[i] in new and i > maxi:
                maxi = i
        print(maxi + 1)



