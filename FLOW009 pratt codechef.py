for _ in range(int(input())):
    quant, price = map(int, input().split())
    if quant > 1000:
        print((quant * price) - (quant * price * 0.1))
    else:
        print(quant * price)
