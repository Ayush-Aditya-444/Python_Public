class Solution:
    def maxScore(self, s: str) -> int:
        sum1=0
        s=list(s)
        for i in range(1,len(s)):
            str1=s[:i]
            str2=s[i:]
            count1=str1.count("0")
            count2=str2.count("1")
            count3=count1+count2
            if sum1<count3:
                sum1=count3
        return sum1
        