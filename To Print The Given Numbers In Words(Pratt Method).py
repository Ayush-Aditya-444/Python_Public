y = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "0": "zero"
}

enter = input('Enter here: ')
new_list = []
for i in enter:
    new_list.append(i)
print(new_list)
for i in range(1, len(new_list) + 1):
    for key, ll in y.items():
        if new_list[i - 1] == key:
            print(ll)
            continue