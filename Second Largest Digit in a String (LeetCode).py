class Solution:
    def secondHighest(self, s: str) -> int:
        s=list(s)
        list1=[]
        for i in range(len(s)):
            if s[i].isnumeric():
                list1.append(int(s[i]))
        a=sorted(list(set(list1)))
        try:
            return a[-2]
        except IndexError:
            return -1