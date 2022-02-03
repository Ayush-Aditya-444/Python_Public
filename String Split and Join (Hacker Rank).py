def split_and_join(line):
    result=line.split()
    p="-".join(result)
    return p
line = input()
result = split_and_join(line)
print(result)