def factorial(m):
    sum, ans = 1, ' '
    for i in range(1, m + 1):
        sum *= i
        if m == 1:
            ans += '1'
        else:
            ans += str(m) + 'x'
            m-=1
    return f'Calculation : {ans}\nFactorial : {sum}'
print(factorial(int(input('Enter Your Number here: '))))