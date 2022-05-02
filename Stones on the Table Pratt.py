n = int(input())
word = input()
p = word[0]
count = 0
for i in range(1, len(word)):
    if word[i] == p:
        count += 1
    else:
        p = word[i]
print(count)