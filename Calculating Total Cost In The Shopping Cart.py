print("Calculating Total Cost In The Shopping Cart:-")
amount = 0
while True:
    condition = input('Do you want to shop? :').lower()
    if condition == "yes":
        pass
    elif condition == "no":
        break
    print("For Apples Of Cost Rs.100/Kg Press 1\nFor Banana Of Cost Rs.80/Kg Press 2\nFor Grapes Of Cost Rs.40/Kg "
          "Press 3")
    num = int(input())
    if num == 1:
        amount += 100
    elif num == 2:
        amount += 80
    elif num == 3:
        amount += 40
    else:
        print("Please Enter The Correct Number")

print(f"Your Total Bill is: {amount}")