class Solution:
    def reformatNumber(self, number: str) -> str:
        dig = ""
        for i in number:
            if i.isnumeric():
                dig += i
        splits = []
        if len(dig) % 3 == 0:
            for i in range(0, len(dig), 3):
                splits.append(dig[i:i+3])
        elif len(dig) % 3 == 1:
            pos = 0
            for i in range((len(dig) // 3) - 1):
                splits.append(dig[pos:pos+3])
                pos += 3
            last_group = dig[-4:]
            splits.extend([last_group[0:2], last_group[2:]])
        else:
            pos = 0
            for i in range((len(dig) // 3)):
                splits.append(dig[pos:pos+3])
                pos += 3
            splits.append(dig[-2:])
        return '-'.join(splits)