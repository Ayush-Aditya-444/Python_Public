class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count1=0
        for i in range(len(s)):
            list1=s[i:i+3]
            set1=set(list1)
            if len(list1)==len(set1) and len(list1)==3:
                count1+=1
        return count1