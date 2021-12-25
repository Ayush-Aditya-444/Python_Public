print("Building A Guessing Game:-")
Secret_Number=10
Guess_Count=0
Guess_Limit=3
while Guess_Count<Guess_Limit:
    x=input("Enter Your Number= ")
    y=int(x)
    if Secret_Number==y:
        print("You Guess The Number Right!!!!")
    else:
        Guess_Count+=1
print("Your Attempts Are Over")