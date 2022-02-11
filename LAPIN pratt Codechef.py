for i in range(int(input())):
    word = input()
    y = int(len(word) / 2)
    word1 = word[:y]
    word2 = word[len(word) - y:]
    if sorted(word1) == sorted(word2):
        print("YES")
    else:
        print("NO")
