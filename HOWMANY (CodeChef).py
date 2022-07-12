num = input()
x = [int(a) for a in str(num)]
if len(x)>=4:
    print("More than 3 digits")
else:
    print(len(x))