for _ in range(int(input())):
    num = input()
    count = 0
    for i in range(len(num)):
        for j in range(i + 1, len(num)):
            for k in range(j + 1, len(num)):
                string = num[i] + num[j] + num[k]
                if string == '007':
                    count += 1
    print(count)

