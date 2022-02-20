for i in range(int(input())):
    Nums = list(map(int, input().split()))
    if Nums[3] == 1:
        Nums[0] += (Nums[2] / 100) * Nums[0]
    elif Nums[3] == 0:
        Nums[0] -= (Nums[1] / 100) * Nums[0]
    print(Nums[0])
