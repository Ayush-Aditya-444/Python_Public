try:
    a=int(input("Enter Your Age:- "))
    b=1000
    c=b/a
    print(c)
    print(a)
except ValueError:
    print("Chutmarike Word Nahi Integer Dena he.")
except ZeroDivisionError:
    print("Abhi Paida Hua he Lode aur Atte Hi Code Enter Karne Laga.")