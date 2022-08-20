class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        s=list(s)
        set1=set(s)
        if len(s)==len(set1):
            return -1
        s1=s[::-1]
        count1=0
        for i in range(len(s)):
            if s.count(s[i])>=2:
                int1=s.index(s[i])
                int2=len(s)-s1.index(s[i])-1
                sum1=int2-int1-1
                if count1<sum1:
                    count1=sum1
        return count1
        