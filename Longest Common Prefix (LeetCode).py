class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        str1,str2=min(strs),max(strs)
        i=0
        while i<len(str1):
            if str1[i]==str2[i]:
                i+=1
            else:
                str1=str1[:i]
        return str1
            