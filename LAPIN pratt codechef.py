for _ in range(int(input())):
    word, stuff, new_word1, new_word2 = input(), {}, '', ''
    if len(word) % 2 == 0:
        for i in range(len(word) // 2):
            new_word1 += word[i]
        for j in range(((len(word) // 2) + 1), len(word)):
            new_word2 += word[j]
        for _ in range(len(word) // 2):
            stuff[new_word1[_]] = word.count(word[_])
    print(stuff)
