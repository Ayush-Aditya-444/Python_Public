def finder_mom(st):
    for i in range(len(st)):
        for j in range(i + 1, len(st)):
            for k in range(j + 1, len(st)):
                String = st[i] + st[j] + st[k]
                if String == 'mom':
                    return k - 1


def finder_dad(ust):
    for i in range(len(ust)):
        for j in range(i + 1, len(ust)):
            for k in range(j + 1, len(ust)):
                String = ust[i] + ust[j] + ust[k]
                if String == 'dad':
                    return k - 1


for _ in range(int(input())):
    n = int(input())
    s = input()
    if finder_mom(s) == finder_dad(s) is None:
        print('Goo-Goo')
    elif finder_mom(s) < finder_dad(s):
        print('Mom')
    elif finder_mom(s) > finder_dad(s):
        print('Dad')

