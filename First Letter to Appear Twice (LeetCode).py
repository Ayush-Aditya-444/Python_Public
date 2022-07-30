class Solution:
    def repeatedCharacter(self, s: str) -> str:
        list1=[]
        for i in range(len(s)):
            if s[i] not in list1:
                list1.append(s[i])
            else:
                return s[i]
        