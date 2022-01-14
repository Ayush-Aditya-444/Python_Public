print("To Print The Given Number In Words:-")
a=(input("Enter Your Number:- "))
print("In Numbers:- ")
print(a)
print("In Words:- ")
Digits_Mapping={
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four",
    "5":"Five",
    "6":"Six",
    "7":"Seven",
    "8":"Eight",
    "9":"Nine",
    "0":"Zero"
}
output=""
for b in a:
    output+=Digits_Mapping.get(b,"!")+" "
print(output)