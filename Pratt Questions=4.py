def Vending_Machine():
    print("Vending Machine:-")
    print("Menu:-")
    print("1. Latte -> $5")
    print("2. Cappucino -> $3.5")
    print("3. Americano -> $7.2")
    print("Press 1 For Latte.")
    print("Press 2 For Cappucino.")
    print("Press 3 For Americano.")
    value=int(input("Press Your Value= "))
    global Milk
    global Water
    global Coffee_Beans
    #Latte
    if (value==1):
        Cash=int(input("Please Enter Cash= "))
        if (Cash>=5):
            if (Milk>=100 and Water>=150 and Coffee_Beans>=50):
                Milk=Milk-100
                Water=Water-150
                Coffee_Beans=Coffee_Beans-50
                Cash=Cash-5
                print("Here's Your Latte")
                if (Cash>0):
                    print(f"Here's Your Reamining ${Cash}")
            else:
                print("Sorry We Dont Have Enough Stuff To Make Your Latte")
        else:
            print("Please Enter More Money")
    #Capi
    if (value==2):
        Cash=float(input("Please Enter Cash= "))
        if (Cash>=3.5):
            if (Milk>=100 and Water>=50 and Coffee_Beans>=100):
                Milk=Milk-100
                Water=Water-50
                Coffee_Beans=Coffee_Beans-100
                Cash=Cash-3.5
                print("Here's Your Cappuccino.")
                if (Cash>0):
                    print(f"Here's Your Reamining ${Cash}")
            else:
                print("Sorry We Dont Have Enough Stuff To Make Your Cappuccino")
        else:
            print("Please Enter More Money")
    #Ameri
    if (value==3):
        Cash=float(input("Please Enter Cash= "))
        if (Cash>=7.2):
            if (Milk>=150 and Water>=50 and Coffee_Beans>=50):
                Milk=Milk-150
                Water=Water-50
                Coffee_Beans=Coffee_Beans-50
                Cash=Cash-7.2
                print("Here's Your Americano.")
                if (Cash>0):
                    print(f"Here's Your Reamining ${Cash}")
            else:
                print("Sorry We Dont Have Enough Stuff To Make Your Americano.")
        else:
            print("Please Enter More Money")
    print(f"Milk Left= {Milk}ml\nWater Left= {Water}ml\nCoffee Beans= {Coffee_Beans}g")
press=int(input("Do You Want To Buy Stuff From Our Shop Press 1 OR Press O To EXIT= "))
Milk=500
Water=500
Coffee_Beans=600
while press==1:
    Vending_Machine()
    press=int(input("Do You Want To Buy Stuff From Our Shop Press 1 OR Press O To EXIT= "))
