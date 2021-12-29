num = int(input('Enter number whose factor tree is to be calculated: '))
fn = num
new_list = []

for i in range(2, num+1):
    j = i
    while num > 0:
        if num % j == 0:
            num //= j
            new_list.append(j)
        else:
            j += 1
        if num == 1:
            break
print(f'Factors of {fn} are as follows:\n{new_list}')