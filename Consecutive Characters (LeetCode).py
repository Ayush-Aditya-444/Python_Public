class Solution:
    def maxPower(self, s: str) -> int:
        max1=0
        count1=0
        for i in range(len(s)-1):
            if s[i]==s[i+1]: 
                count1+=1
                if max1<count1:
                    max1=count1
            else:
                count1=0
        return max1+1