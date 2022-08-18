class Solution:
    def greatestLetter(self, s: str) -> str:
        list1=[""]
        s=list(s)
        for i in range(len(s)):
            str1=s[i].lower()
            str2=s[i].upper()
            if str1 in s and str2 in s:
                list1.append(str2)
        return max(list1)