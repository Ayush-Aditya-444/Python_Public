class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        s=list(s)
        str1=[]
        for i in range(len(words)):
            str1=str1+list(words[i])
            if str1==s:
                return True
        return False
        