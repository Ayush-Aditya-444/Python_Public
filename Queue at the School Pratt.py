a, b = map(int, input().split())
text = input()
word = [i for i in text]
j = 0
for ki in range(b):
    while j <= len(word):
        try:
            if word[j] == 'B' and word[j + 1] == 'G':
                word[j], word[j + 1] = word[j + 1], word[j]
                j += 1
        except IndexError:
            break
        j += 1
    j = 0
print("".join(word))
