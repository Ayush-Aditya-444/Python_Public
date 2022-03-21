number_of_input=int(input())
for i in range(number_of_input):
    number_of_tyres=int(input())
    if number_of_tyres%4==0:
        print("NO")
    else:
        print("YES")