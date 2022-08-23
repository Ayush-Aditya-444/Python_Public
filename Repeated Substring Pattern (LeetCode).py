class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        str1=""
        for i in range(len(s)-1):
            str1+=s[i]
            if len(s)%len(str1)==0:
                if str1*(len(s)//len(str1))==s:
                    return True
        return False