for _ in range(int(input())):
    a = int(input())
    word = input()
    if 'I' in word:
        print('INDIAN')
    elif 'Y' in word:
        print('NOT INDIAN')
    else:
        print('NOT SURE')