def mutate_string(string, position, character):
    b=list(string)
    b[position]=character
    a="".join(b)
    return a
s = input()
i, c = input().split()
s_new = mutate_string(s, int(i), c)
print(s_new)