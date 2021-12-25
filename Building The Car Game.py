print("Building The Car Game:-")
command1="Start"
command2="Stop"
command3="Quit"
command4="Help"
x=input("Enter Your Command=")
if x=="Start":
    print("Car started . . . Ready To Go!")
elif x=="Stop":
    print("Car Stopped")
elif x=="Quit":
    print("The Game Has Been Quit")
elif x=="Help":
    print("Start - To Start The Car")
    print("Stop - To Stop The Car")
    print("Quit - To Exit")
else:
    print("I Don't Understand That ...")